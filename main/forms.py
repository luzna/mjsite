# -*- coding: utf-8 -*-
from django import forms
from .models import Comment

class ContactForm(forms.Form):
    user = forms.CharField(required=True, label = "Nick")
    contact_email = forms.EmailField(required=True, label = "E-mail zwrotny")
    title = forms.CharField(required=True, label = "Tytuł wiadomości")
    content = forms.CharField(
        required = True,
        widget = forms.Textarea,
        label = "Treść"
    )

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('nickname', 'comment',)