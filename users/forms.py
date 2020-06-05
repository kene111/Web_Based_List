from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField() #you can sett Required = False, meaning it is not compulsory to fill email.

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
