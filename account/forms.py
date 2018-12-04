import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class AddUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    teacher = forms.BooleanField(widget=forms.CheckboxInput())

    def save(self):
        User.objects.create( username=self.cleaned_data['username'],
                             password=self.cleaned_data['password'],
                             first_name=self.cleaned_data['first_name'],
                             last_name=self.cleaned_data['last_name'],
                             email=self.cleaned_data['email']
                             )
        if self.cleaned_data['teacher']==True:
            user = User.objects.get(username=self.cleaned_data['username'])
            User.objects.filter(id=user.id).update(is_staff=True)
