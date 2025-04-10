from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
def word_count_validator(value):
    word_count = len(value.split())
    if word_count > 300:
        raise ValidationError('Абзац не должен превышать 300 слов.')




class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class Paragraph(models.Model):
    content = models.TextField(unique=True, validators=[word_count_validator])
    essay = models.ForeignKey('Essay', on_delete=models.CASCADE, related_name='paragraphs')

    def __str__(self):
        return self.content[:50] + '...'
    
    
class Podcast(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    banner = models.ImageField(upload_to='podcast_banners/', null=True, blank=True)
    banner_url = models.URLField(null=True, blank=True)
    video = models.FileField(upload_to='podcast_videos/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title
    def get_video(self):
        if self.video:
            return self.video.url
        return self.video_url
    

    def clean(self):
        if self.banner and self.banner_url:
            raise ValidationError("Please provide either a local banner or a banner URL — not both.")
        if not self.banner and not self.banner_url:
            raise ValidationError("You must provide a banner — either a local file or a URL.")

        if self.video and self.video_url:
            raise ValidationError("Please provide either a local video or a video URL — not both.")
        if not self.video and not self.video_url:
            raise ValidationError("You must provide a video — either a local file or a URL.")
class Essay(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    theme = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    cotegory = models.CharField(max_length=50)
    
    def paragraph(self):
        return Paragraph.objects.filter(essay=self)
    # def questions(self):
    #     return QuestionForEssay.objects.filter(essay=self)
    def __str__(self):
        return self.title
class Paragraph(models.Model):
    content = models.TextField(unique=True, validators=[word_count_validator])
    essay = models.ForeignKey(Essay, related_name='paragraphs', on_delete=models.CASCADE)

    def __str__(self):
        return f"Абзац для эссе: {self.essay.title}"

class QuestionForEssay(models.Model):
    question = models.CharField(max_length=120)
    essay = models.ForeignKey(Essay,related_name='questions',on_delete=models.CASCADE)
    def __str__(self):
        return f'question: {self.question}'


class Comment(models.Model):
    essay = models.ForeignKey(Essay, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


    
    

    def __str__(self):
        return f"Comment by {self.user.username} on {self.essay.title}"







# books mode ----------------------------
class Book(models.Model):
    title = models.CharField(max_length=70)
    short_description = models.CharField(max_length=90)
    banner = models.ImageField(upload_to='media/', null=True, blank=True)
    banner_url = models.URLField(null=True, blank=True)
    theme_title = models.CharField(max_length=90)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=130)
    def __str__(self):
        return self.title

    def get_banner(self):
        if self.banner:
            return self.banner.url
        return self.banner_url

    def clean(self):
        if self.banner and self.banner_url:
            raise ValidationError("Пожалуйста, укажите либо локальный баннер, либо URL — не оба сразу.")
        if not self.banner and not self.banner_url:
            raise ValidationError("Вы должны указать баннер — либо файл, либо URL.")


class BookThemes(models.Model):
    theme = models.TextField()
    book = models.ForeignKey(Book, related_name='themes', on_delete=models.CASCADE)

    def __str__(self):
        return f"Тема: {self.theme}"


class BookComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')


    def __str__(self):
        return self.content[:30]
    
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Этот юзернейм уже занят.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Пароли не совпадают.")
        return cleaned_data
    
    
    
    
    



# forum -----------------

class ForumMessage(models.Model):
    topic = models.ForeignKey('ForumTopic', related_name='messages', on_delete=models.CASCADE)  # связь с ForumTopic
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # связь с автором сообщения
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Message by {self.author.username} in {self.topic.title}"
    

class ForumTopic(models.Model):
    title = models.CharField(max_length=255)  # название темы
    content = models.TextField(blank=True, null=True)  # описание темы
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # пользователь, который создал тему
    created_at = models.DateTimeField(auto_now_add=True)  # время создания темы

    def __str__(self):
        return self.title

    # Связь с сообщениями через поле 'messages', которое хранит все сообщения в теме
    # Это поле автоматически будет создано благодаря связи 'ForeignKey' в модели ForumMessage
    # messages = models.ForeignKey(ForumMessage, related_name='topic_messages', on_delete=models.CASCADE)  # Ненужно










class ContactMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name or self.user.username} — {self.email}"