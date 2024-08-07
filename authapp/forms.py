from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class RegistrationForm(UserCreationForm):
    # add more fields to the existing fields in the user creation form 
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['username','first_name','email','password1','password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','subtitle','body']
        