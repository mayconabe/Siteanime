# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class UserModelForm(ModelForm):
	User._meta.get_field('email').blank = False
	class Meta:
		model = User
		fields = ['username', 'password', 'email']
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control', 'max-length':18}),
			'password': forms.PasswordInput(attrs={'class': 'form-control', 'max-length':100}),
			'email': forms.TextInput(attrs={'class': 'form-control', 'max-length':100}),
		}

		error_messages = {
			'username': {
				'required': 'Este campo é obrigatório.'
			},
			'password': {
				'required': 'Este campo é obrigatório.'
			},
			'email': {
				'required': 'Escreva um email válido.'
			}
		}

class LoginForm(ModelForm):

	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'password']
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control', 'max-length':18}),
			'password': forms.PasswordInput(attrs={'class': 'form-control', 'max-length':100}),
		}

		error_messages = {
			'username': {
				'required': 'Este campo é obrigatório.'
			},
			'password': {
				'required': 'Este campo é obrigatório.'
			},
		}


	def clean(self, *args, **kwargs):
		username = self.cleaned_data('username')
		password = self.cleaned_data('password')

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError('O usuario não existe')
			if not user.forms.check_password(password):
				raise forms.ValidationError('Senha Incorreta')
			if not user.is_active:
				raise forms.ValidationError('O usuario não está ativo')
		return super(LoginForm, self).clean(*args, **kwargs)


