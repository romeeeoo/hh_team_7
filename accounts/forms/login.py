from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Your username')
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)
