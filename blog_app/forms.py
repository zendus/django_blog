from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from blog_app.models import Comment
User._meta.get_field('email')._unique = True

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('opinion',)


class UserSignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']