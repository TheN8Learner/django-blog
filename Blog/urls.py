from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('blog/<int:pk>/', views.article_details, name="article_details"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<int:pk>/', views.posts_by_category, name='category'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
