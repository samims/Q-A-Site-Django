from django.contrib.auth.models import User
from django import forms
from .models import Answer, Question


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['title', 'description']


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['answer_text']
