from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Post
        fields = ('id', 'title','author', 'created_date', 'img', 'price', 'tag')
        read_only_fields = ('id', 'title','author', 'created_date', 'img', 'price', 'tag')
# Views
