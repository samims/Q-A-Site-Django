from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db.models import Count
import pytz
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse, HttpResponse, get_object_or_404
from django.utils import timezone
from .models import Question, Answer, Upvote


# index page of the site  and ans app
def index(request):
    latest_questions = Question.objects.all().order_by('-pub_date')[:10][::-1]
    context = {'latest_questions': latest_questions}
    return render(request, template_name='ans/index.html', context=context)


# What are the answers to a given question?
def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    answers = question.answer_set.all()

    context = {'question': question, 'answers': answers, }
    if request.method == 'POST':
        if request.user.is_authenticated():
            user = request.user
            if request.POST['type'] == 'vote':
                answer = Answer.objects.get(pk=request.POST['answer_id'])
                upvote = Upvote.objects.get_or_create(user=user, answer=answer)
            elif request.POST['type'] == 'answer':
                ans = request.POST['write']
                new_ans = Answer.objects.create(questions=question, user=user, answer_text=ans, pub_date=timezone.now())
                new_ans.save()

            return HttpResponseRedirect(reverse('ans:detail', args=(question_id,)))
        else:
            return 'User is not logged in'

    return render(request, template_name='ans/detail.html', context=context)


# 1. What are the questions asked by me?"
def asked_by_me(request, userid):
    user = User.objects.get(pk=userid)
    questions = user.question_set.all()
    context = {'questions': questions, 'user_id': userid}
    return render(request, template_name='ans/asked_by_me.html', context=context)


# What are the answers given by me?
def answered_by_me(request, userid):
    user = User.objects.get(pk=userid)
    answers = user.answer_set.all()

    questions = user.question_set.all()
    context = {'answers': answers, 'questions': questions, 'user_id': userid}
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
def upvoted_by_me(request, userid):
    user = User.objects.get(pk=userid)
    upvoted = user.upvote_set.all()
    context = {'upvoted': upvoted}
    return render(request, template_name='ans/upvoted_by_me.html', context=context)


# Across the entire application, which question has had the highest number of upvotes over the past hour.
def question_of_hour(request):
    last_answer = Answer.objects.filter(pub_date__gte=timezone.now() - timedelta(hours=1))
    # print(last_answer.extra(select))
    incr=None
    vote_count = None
    old_vote_count = last_answer[0].upvote_set.all().count()
    print(old_vote_count)
    temp = 0
    try:
        ans_of_hour = [last_answer[0]]

    except IndexError:
        ans_of_hour = None

    else:
        incr = 0
        for answr in last_answer:
            vote_count = 0
            vote_count += Upvote.objects.filter(answer_id=answr.id).count()
            if old_vote_count < vote_count:
                ans_of_hour[incr] = answr

                old_vote_count = vote_count

            elif old_vote_count == vote_count:
                ans_of_hour.append(answr)

                incr += 2

    print(ans_of_hour)
    # context = {'question': qsn_of_the_hour, 'vote': old_vote_count}
    context = {'answer_of_hour': ans_of_hour, 'temp': incr, 'vote': vote_count}
    return render(request, template_name='ans/ans_of_hour.html', context=context)


#

# Across the entire application, which question has had the highest number of votes ever.
def question_of_the_site(request):
    pass
#     questions = Question.objects.all()
#     old_vote_count = 0
#     qsn_of_the_site = questions[0]
#     for qsn in questions:
#         vote_count = 0
#         ans = Answer.objects.filter(questions_id=qsn.id)
#         for a in ans:
#             vote_count += Upvote.objects.filter(answer_id=a.id).count()
#         if old_vote_count < vote_count:
#             qsn_of_the_site = qsn
#             old_vote_count = vote_count
#
#     context = {'question': qsn_of_the_site, 'vote': old_vote_count}admin
#
#     return render(request, template_name='ans/question_of_site.html', context=context)
