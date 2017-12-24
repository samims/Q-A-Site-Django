from django import forms


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=35)
    last_name = forms.CharField(label='Last Name', max_length=30)
    username = forms.CharField(required=True, label='Username', max_length=25)
    email = forms.CharField(required=True, label='Email', max_length=40)
    password = forms.CharField(required=True, label='Password', widget= forms.PasswordInput())











# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
#
# class RegistrationForm(UserCreationForm):
#     first_name = forms.CharField(max_length=25, required=False)
#     last_name = forms.CharField(max_length=20, required=False)
#     email = forms.EmailField(max_length=30, required=False)
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
#
#
