from django.contrib.auth.models import User
from django.db import models


# Question table connected with User by foreignkey user
class Question(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    pub_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Answer Table connected User by user foreign key
class Answer(models.Model):
    answer_text = models.TextField()
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer_text


# connected with both User and Answers
class Upvote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
