from django import forms
from .models import Book , Photo , UserProfile
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields =('title','author','pdf')


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file', )

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('city','age')
