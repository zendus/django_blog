from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth import REDIRECT_FIELD_NAME, views as auth_views
from . import views

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('posts/<int:pk>/', views.read_post, name='read_post'),
    path('articles/', views.all_articles, name='all_articles'),
    path('poems/', views.all_poems, name='all_poems'),
    path('quotesandvibes/', views.all_yarns, name='all_yarns'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='blog_app/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup')
]