from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('posts/<int:pk>/', views.read_post, name='read_post'),
    path('articles/', views.all_articles, name='all_articles'),
    path('poems/', views.all_poems, name='all_poems'),
    path('quotesandvibes/', views.all_yarns, name='all_yarns'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup')
]