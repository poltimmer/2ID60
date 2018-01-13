from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from blog.models import Post

class DetailsView(generics.RetrieveAPIView):
    """This class handles the http GET requests."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CreateView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
