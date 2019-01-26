from django.contrib.auth.forms import *
from .models import *
from django import forms


class TeacherCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Teacher
        fields = ('username','password','name','surname','name','second_name')


class TeacherChangeForm(UserChangeForm):
    class Meta(UserCreationForm):
        model = Teacher
        fields = ('username','password','name','surname','name','second_name')


