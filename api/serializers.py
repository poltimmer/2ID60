from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Post
        fields = ('title', 'text', 'date_modified', 'skills', 'tags', 'jobType', 'price')
        read_only_fields = ('creator', 'created_date', 'published_date', 'postType', 'downloads')
# Views
