from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.
posts = []


def home(request):
    return redirect('login')


class PostListView(ListView):
    model = Post
    template_name = 'connect/profile.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['constent','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['constent','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    fields = ['constent','image']
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
    



def profile(request):
    context = {
        'title': 'My Posts',
        'posts': Post.objects.all(),
    }
    return render(request, 'connect/profile.html', context)


def create(request):
    return render(request, 'connect/create.html', {'title': 'Create Post'})

def saving(request,pk):
    obj = Post.objects.get(pk=pk)
    obj.savePost = True
    obj.save()
    return redirect('connect-profile')

def unsaving(request,pk):
    obj = Post.objects.get(pk=pk)
    obj.savePost = False
    obj.save()
    return redirect('connect-profile')

@login_required
def saved(request):
    context = {
        'title': 'Saved Posts',
        'posts': Post.objects.all(),
    }
    return render(request, 'connect/saved.html', context)

@login_required
def posts(request):
    context = {
        'title': 'All Posts',
        'posts': Post.objects.all(),
    }
    return render(request, 'connect/posts.html', context)