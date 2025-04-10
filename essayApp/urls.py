from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='home'),
    path('books/', book, name='book'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('contact/', contact_view, name='contact'),
    path('essay/', essay, name='essay'),
    path('essay/<int:pk>/', essay_detail, name='essay_detail'),
    path('forum/', forum, name='forum'),
    path('forum/topic/<int:id>/', room, name='topic_detail'),
    path('forum/create/', create_topic, name='create_forum_topic'),
    path('login/', login, name='login'),
    path('podcasts/',podcasts, name='podcasts'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
