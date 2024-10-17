from django import forms
from django.contrib.auth.models import User
from .models import Blogs
class Authorization(forms.Form):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-inpput'}))

class FormForNotes(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'preview', 'content']
    # title =forms.CharField(label ='Заголовок')
    # preview = forms.CharField(label='Текст для предпросмотра')
    # content = forms.TextInput(label='Содержание')
    # pablished = forms.DateField(label='Дата публикации')
    