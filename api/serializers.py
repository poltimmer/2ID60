from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Post
        fields = ('title','author', 'created_date', 'published_date', 'postType', 'downloads', 'img', 'text', 'skills', 'tags', 'jobType', 'price')
        read_only_fields = ('title','author', 'created_date', 'published_date', 'postType', 'downloads', 'img', 'text', 'skills', 'tags', 'jobType', 'price')
# Views
