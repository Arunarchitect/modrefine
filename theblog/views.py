from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
# Create your views here.
# def home(request):
#     return render(request, 'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class CreatePostView(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = '__all__'
    # fields = ('title','body')