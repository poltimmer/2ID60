from django.db import models
from django.utils import timezone


class Post(models.Model):
    creator = models.ForeignKey('auth.User') #formerly 'author'
    title = models.CharField(max_length=200)
    text = models.TextField() #description
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    postType = False #photo or job, could do 1 or 2.
    imgUrl = '' #for postType photo. url to image, likely local. (not from the web)
    skills = [] #for postType job. a list of skills required. could also be a dictionary.
    tags = [] #for postType photo. a list of tags for a picture. (landscape, nature, portrait) could also be a dictionary.
    jobType = [] #lists what job types the job belongs to. (webdesign, modeling, 3d render) Should just merge this with tags, but not with skills!
    downloads = 0 # for postType photo

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
