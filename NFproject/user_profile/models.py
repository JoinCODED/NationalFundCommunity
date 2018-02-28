from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.
class Profile (models.Model):

    TYPE_CHOICES =(
    ("I","Individual"),
    ("O","Orginization")
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=1,choices=TYPE_CHOICES)
    bio = models.TextField()
    my_website = models.URLField()
    age = models.IntegerField()
    slug= models.SlugField(blank=True)


@receiver (pre_save, sender= Profile)
def add_slug_to_Profile (sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.user.username)
