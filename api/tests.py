from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User
class ModelTestCase(TestCase):
    """This class defines the test suite for the post model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.title = "test"
        self.post = Post(title=self.title)
        
    def test_model_can_create_a_post(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Post.objects.count()
        self.post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)
# Create your tests here.
