from django.shortcuts import render

# Create your views here.
posts = []


def home(request):
    return render(request, 'connect/login.html', {'title': 'Login'})


def profile(request):
    context = {
        'title': 'My Posts',
        'posts': ['10 likes','23 likes', '57 likes', '91 likes' ,'123 likes'],
    }
    return render(request, 'connect/profile.html', context)

def create(request):
    return render(request, 'connect/create.html', {'title': 'Create Post'})

def posts(request):
    context = {
        'title': 'All Posts',
        'posts': ['10 likes','23 likes', '57 likes', '91 likes' ,'123 likes'],
    }
    return render(request, 'connect/posts.html', context)