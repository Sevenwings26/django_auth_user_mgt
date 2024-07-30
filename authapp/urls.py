from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('create_post/', views.createPost, name="create_post"),
    path('sign-up/', views.register, name="sign-up"),
]