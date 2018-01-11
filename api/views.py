from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from blog.models import Post

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Save the POST data when creating a new post."""
        serializer.save()
# Create your views here.

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
