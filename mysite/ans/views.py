import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse, HttpResponse
from django.utils import timezone
from .models import Question, Answer, Upvote


# index page of the site  and ans app
def index(request):
    latest_questions = Question.objects.all()
    context = {'latest_questions': latest_questions}
    return render(request, template_name='ans/index.html', context=context)


# What are the answers to a given question?
def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    answers = question.answer_set.all()
    # print(answers)
    # ans_id = request.POST.get('answer.id')
    # vote_count = Upvote.objects.filter(user__isnull=False, answer=1).count()
    votes = Upvote.objects.filter(answer__in=answers)
    # # vote_count = [x for x in votes[range(len(votes))]]
    vote_count = {}
    v = 0
    for x in range(len(votes)):
        z = votes[x].answer_id
        if z not in vote_count.keys():
            vote_count[z] = 1
        else:
            vote_count[z] += 1

    context = {'question': question, 'answers': answers, 'vote_count': vote_count}
    if request.method == 'POST':
        if request.user.is_authenticated():
            user = request.user
            type = request.POST['type']
            if type == 'vote':
                answer = Answer.objects.get(pk=request.POST['answer_id'])
                upvote = Upvote.objects.create(user=user, answer=answer)
                upvote.save()
            elif type == 'answer':
                ans = request.POST['write']
                new_ans = Answer.objects.create(questions=question, user=user, answer_text=ans, pub_date=timezone.now())
                new_ans.save()

            return HttpResponseRedirect(reverse('ans:detail', args=(question_id,)))
        else:
            return 'User is not logged in'
    
    return render(request, template_name='ans/detail.html', context=context)


# 1. What are the questions asked by me?"
def asked_by_me(request, user_id):
    user = User.objects.get(pk=user_id)
    questions = user.question_set.all()
    context = {'questions': questions, 'user_id': user_id}
    return render(request, template_name='ans/asked_by_me.html', context=context)


# What are the answers given by me?
def answered_by_me(request, user_id):
    user = User.objects.get(pk=user_id)
    answers = user.answer_set.all()
    questions = user.question_set.all()
    context = {'answers': answers, 'questions': questions, 'user_id': user_id}
    return render(request, template_name='ans/answered_by_me.html', context=context)


#
# def vote(request, question_id):
#     question = Question.obects.get(pk=question_id)
#
#     if request.method == 'POST':
#         if request.form.is_valid():
#             user = request.user.is_authenticated()
#
#             upvote = Upvote.objects.create(user=user, answer=answer)
#
#             upvote.save()
#             return HttpResponseRedirect(reverse('ans:detail', args=(question_id,)))


# What are the upvotes done by me?
def upvoted_by_me(request, user_id):
    user = User.objects.get(pk=user_id)
    upvote = user.upvote_set.all()
    ans_id = []
    for x in range(len(upvote)):
        ans_id.append(upvote[x].answer_id)

    ans = Answer.objects.filter(pk__in=ans_id)
    context = {'answers': ans}

    return render(request, template_name='ans/upvoted_by_me.html', context=context)


# Across the entire application, which question has had the highest number of upvotes over the past hour.
def question_of_hour(request):
    start_time = datetime.datetime.now()
    end_time = start_time - datetime.timedelta(hours=1)
    # last_hour = Question.objects.filter(created_document_timestamp__gte=end_time)
    # Model.objects.filter(time_stamp__range=(start_date, end_date))

    time_1_hours_ago = datetime.datetime.now() - datetime.timedelta(hours=1)
    last_hour = Question.objects.filter(pub_date__gte=time_1_hours_ago)
    old_vote_count = 0
    try:
        qsn_of_the_hour = last_hour[0]
    except IndexError:
        qsn_of_the_hour = None
    else:
        for qsn in last_hour:
            vote_count = 0
            ans = Answer.objects.filter(questions_id=qsn.id)
            for a in ans:
                vote_count += Upvote.objects.filter(answer_id=a.id).count()
            if old_vote_count < vote_count:
                qsn_of_the_hour = qsn
                old_vote_count = vote_count

    context = {'question': qsn_of_the_hour, 'vote': old_vote_count}
    return render(request, template_name='ans/ans_of_hour.html', context=context)


# Across the entire application, which question has had the highest number of votes ever.
def question_of_the_site(request):
    questions = Question.objects.all()
    old_vote_count = 0
    qsn_of_the_site = questions[0]
    for qsn in questions:
        vote_count = 0
        ans = Answer.objects.filter(questions_id=qsn.id)
        for a in ans:
            vote_count += Upvote.objects.filter(answer_id=a.id).count()
        if old_vote_count < vote_count:
            qsn_of_the_site = qsn
            old_vote_count = vote_count

    context = {'question': qsn_of_the_site, 'vote': old_vote_count}

    return render(request, template_name='ans/question_of_site.html', context=context)
