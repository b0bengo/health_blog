from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class Homepage(ListView):
    """
    This view handles the homepage of the blog. It uses ListView to display a list of blog posts.
    """
    model = Post
    template_name = 'index.html'