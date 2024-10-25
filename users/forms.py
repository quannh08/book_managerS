from django import forms

class registerForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=50,widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50,widget=forms.PasswordInput)

class loginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput)