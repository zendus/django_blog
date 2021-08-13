from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('posts/<int:pk>/', views.read_post, name='read_post'),
]