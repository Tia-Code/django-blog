from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from blogging.models import Post

# Class-based ListView for displaying posts
class PostListView(ListView):
    template_name = "blogging/list.html"
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')

# Class-based DetailView for displaying a single post
class PostDetailView(DetailView):
    template_name = "blogging/detail.html"
    model = Post

    def get_queryset(self):
        # Filter only published posts
        return Post.objects.exclude(published_date__exact=None)
