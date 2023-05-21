from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('chatroom/<int:pk>', views.chatroom, name='chatroom'),
    # path('post/<int:pk>/save/', views.saving, name='post-save'),
    # path('post/<int:pk>/unsave/', views.unsaving, name='post-unsave'),

]
