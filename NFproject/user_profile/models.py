from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.
class Individual_Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()
    my_website = models.URLField()
    age = models.IntegerField()#individual
    interest=models.CharField(max_length=200)#individual
    slug= models.SlugField(blank=True)


class Orginization_Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()
    my_website = models.URLField()
    slug= models.SlugField(blank=True)
    location_name=models.CharField(max_length=200)#orginization
    location_URL=models.URLField()#orgn


@receiver (pre_save, sender= Individual_Profile)
def add_slug_to_Individual_Profile (sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.user.username)

@receiver (pre_save, sender=  Orginization_Profile)
def add_slug_to_Orginization_Profile (sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.user.username)
