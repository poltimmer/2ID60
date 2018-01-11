from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
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
    price = models.CharField(max_length=7, default="15,00") #for photo

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilepicture = models.ImageField(upload_to = 'img/', default = 'img/emptyPP.png')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
