# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

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
