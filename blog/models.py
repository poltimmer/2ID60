from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
import os
from uuid import uuid4
from multiselectfield import MultiSelectField

def wrapper():
    return
def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, null=True, blank=True) #formerly 'author'
    title = models.CharField(max_length=200)
    text = models.TextField() #description
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    img = models.ImageField(upload_to = path_and_rename('img/')) #for postType photo. url to image, likely local. (not from the web)
    tags = [] #for postType photo. a list of tags for a picture. (landscape, nature, portrait) could also be a dictionary.
    downloads = 0 # for postType photo
    price = models.PositiveIntegerField() #for photo

    TAG_CHOICES = (
        ('Portrait', 'Portrait'),
        ('Landscape', 'Landscape'),
        ('Black & White', 'Black & White'),
        ('Fashion','Fashion'),
        ('Film','Film'),
        ('Nature', 'Nature'),
        ('Food','Food'),
        ('Music','Music'),
        ('Sports','Sports'),
        ('Automotive', 'Automotive'),
        ('Travel','Travel'),
    )
    tag = MultiSelectField(choices = TAG_CHOICES, blank=True, null=True)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilepicture = models.ImageField(upload_to = 'img/', default = 'img/emptyPP.png')
    following = []


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




# follow system
'''
class Followage(models.Model):
  from_user = models.ForeignKey(
    User, related_name='follower'
  )
  to_user = models.ForeignKey(
    User, related_name='to_be_followed'
  )
  def __unicode__(self):
    return u'%s, %s' % (
      self.from_user.username,
      self.to_user.username
    )
  class Meta:
    unique_together = (('to_user', 'from_user'), )
'''
