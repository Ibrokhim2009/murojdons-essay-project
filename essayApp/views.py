from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.urls import reverse
from django.core.exceptions import ValidationError
from .forms import *
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
def word_count_validator(value):
    word_count = len(value.split())
    if word_count > 300:
        raise ValidationError(f'Абзац не должен содержать более 300 слов. Сейчас: {word_count}.')

# Create your views here.
def index(request):
    ctx={}
    return render(request,'index.html',ctx)

def book(request):
    books = Book.objects.all()
    ctx={
        'books': books
    }
    
    return render(request,'books.html',ctx)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    comments = book.comments.all()
    form = BookCommentForm()

    if request.method == 'POST':
        form = BookCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.user = request.user
            comment.save()
            return redirect('book_detail', pk=book.pk)

    context = {
        'book': book,
        'comments': comments,
        'form': form,
    }
    return render(request, 'book-comments.html', context)





def essay(request):
    essays = Essay.objects.all()
    ctx={
        'essays': essays
    }
    return render(request,'essay.html',ctx)

def essay_detail(request, pk):
    essay = get_object_or_404(Essay, id=pk)
    comments = essay.comments.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(reverse('login') + f'?next={request.path}')

        content = request.POST.get('content')
        if content:  # Проверим, что не пусто
            Comment.objects.create(essay=essay, user=request.user, content=content)

        return redirect('essay_detail', pk=essay.id)  # Чтобы избежать повторной отправки

    return render(request, 'fool-essay.html', {'essay': essay, 'comments': comments})




def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Логиним пользователя
            return redirect('home')  # Перенаправляем на домашнюю страницу
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Проверка на существование пользователя с таким именем
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Пользователь с таким именем уже существует.')  # Добавляем ошибку в форму
            else:
                # Сохраняем пользователя
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])  # Хешируем пароль
                user.save()

                # Аутентификация пользователя
                user = authenticate(username=user.username, password=form.cleaned_data['password'])

                if user is not None:
                    auth_login(request, user)  # Логиним пользователя

                    # Перенаправляем на главную страницу
                    return redirect('home')  # 'home' должен быть именем вашего пути главной страницы
        else:
            # Если форма невалидна, возвращаем форму с ошибками
            return render(request, 'register.html', {'form': form})
    else:
        # Если метод GET, отображаем пустую форму
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})













def podcasts(request):

    podc = Podcast.objects.all()
    ctx={
        'podcasts': podc
    }
    return render(request,'podcasts.html',ctx)



from django.shortcuts import render, redirect
from .models import ForumTopic, ForumMessage
from .forms import ForumTopicForm, ForumMessageForm

def forum(request):
    # Получаем все темы форума
    topics = ForumTopic.objects.all()
    for topic in topics:
        # Подсчитываем количество сообщений (комментариев) для каждой темы
        topic.comments_count = topic.messages.count()  # Используем 'messages' вместо 'comments'
    return render(request, 'forum.html', {'topics': topics})

def create_topic(request):
    if request.method == 'POST':
        form = ForumTopicForm(request.POST)
        if form.is_valid():
            forum_topic = form.save(commit=False)
            forum_topic.created_by = request.user  # Устанавливаем автора
            forum_topic.save()
            return redirect('forum')  # Перенаправляем на страницу форума
    else:
        form = ForumTopicForm()
    return render(request, 'create_forum_topic.html', {'form': form})

def room(request, id):
    topic = ForumTopic.objects.get(id=id)
    messages = ForumMessage.objects.filter(topic=topic).order_by('created_at')  # Загружаем все сообщения для этой темы
    for message in messages:
        message.is_user_message = message.author.username == request.user.username
    if request.method == 'POST':
        form = ForumMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.topic = topic  # Связываем сообщение с темой
            message.author = request.user  # Устанавливаем автора сообщения
            message.save()
            return redirect('topic_detail', id=topic.id)  # Перенаправляем на страницу с этой темой, чтобы обновить список сообщений
    else:
        form = ForumMessageForm()

    return render(request, 'forum_topic_detail.html', {
        'topic': topic,
        'messages': messages,
        'form': form,
        'user': request.user
    })








def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, user=request.user)
        if form.is_valid():
            message = form.save(commit=False)
            if request.user.is_authenticated:
                message.user = request.user
                message.name = request.user.get_full_name() or request.user.username
            message.save()
            return redirect('/')  # Перенаправление на страницу успеха
    else:
        form = ContactForm(user=request.user)

    return render(request, 'contact.html', {'form': form})