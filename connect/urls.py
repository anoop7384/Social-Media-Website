from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='connect-home'),
    path('profile/', views.profile, name='connect-profile'),
    path('create/', views.create, name='connect-create'),
    path('posts/', views.posts, name='connect-posts'),
]