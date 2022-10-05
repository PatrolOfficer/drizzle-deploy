from django.shortcuts import render, get_object_or_404
from .models import Post
from  django.views.generic import (ListView, 
                                    DetailView, 
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
                                    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from taggit.models import Tag
from django.db.models import Q


def home(request, tag_slug=None):
    posts = Post.objects.all()
    # tag post
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    
    # tags = Tag.objects.filter(id__in=Post.objects.all().values('tags'))
    
    #search
    q= request.GET['q']
    if q is not None:
        multiple_q=Q(Q(title__icontains=q) | Q(content__icontains=q))
        posts=Post.objects.filter(multiple_q)


    return render(request, 'blog/home.html', {'posts':posts})

class PostListView(ListView):
    model=Post
    template_name = 'blog/home.html'    # <app>/<model>_<viewtype>.html
    context_object_name= 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

    

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model=Post



class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields = ['title', 'image', 'content', 'tags']
    permission_required = "blog.add_post"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Post
    fields = ['title','image', 'content', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Post
    success_url = '/'
    permission_required = "blog.delete_post"
        
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class LatestPostView(ListView):
    model=Post
    template_name = 'blog/latest_post.html'    # <app>/<model>_<viewtype>.html
    context_object_name= 'posts'
    ordering = ['-date_posted']

def announcements(request):
    return render(request, 'blog/announcements.html', {'title':'Announcements'})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})