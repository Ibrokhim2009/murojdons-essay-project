from django import forms
from django.contrib.auth.models import User
from .models import *
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают.")
        return cleaned_data




class BookCommentForm(forms.ModelForm):
    class Meta:
        model = BookComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your comment...'}),
        }





from django import forms
from .models import ForumTopic, Comment

# Форма для создания темы
class ForumTopicForm(forms.ModelForm):
    class Meta:
        model = ForumTopic
        fields = ['title','content'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ForumMessageForm(forms.ModelForm):
    class Meta:
        model = ForumMessage
        fields = ['content']
        
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user and user.is_authenticated:
            self.fields['name'].widget = forms.HiddenInput()
            self.fields['name'].required = False
            self.initial['name'] = user.get_full_name() or user.username

