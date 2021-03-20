# -*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={})
    )
    password = forms.CharField(
        required=True,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={})
    )
