from django.urls import path
from blogging.views import PostListView, PostDetailView  # Import the new class-based views

urlpatterns = [
    path('', PostListView.as_view(), name="blog_index"),  # List view
    path('posts/<int:pk>/', PostDetailView.as_view(), name="blog_detail"),  # Detail view
]