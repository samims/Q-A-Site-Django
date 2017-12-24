from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            username = form_data['username']
            first_name = form_data.get('first_name')
            last_name = form_data.get('last_name')
            email = form_data['email']
            password = form_data['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)

                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('username and password already exists')

    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})


