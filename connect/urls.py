from django.urls import path
from . import views
from users import views as loginV
from .views import PostListView, PostDetailView,PostCreateView, PostUpdateView, PostDeleteView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='connect-home'),
    path('profile/', PostListView.as_view(), name='connect-profile'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='connect-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/save/', views.saving, name='post-save'),
    path('post/<int:pk>/unsave/', views.unsaving, name='post-unsave'),
    path('post/<int:pk>/like/', views.liked, name='post-like'),
    path('post/<int:pk>/unlike/', views.unliked, name='post-unlike'),
    path('posts/', views.posts, name='connect-posts'),
    path('posts/saved', views.saved, name='connect-saved'),
    path('posts/account/<int:pk>', views.user_posts, name='post-account'),
]


# urlpatterns += static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)

