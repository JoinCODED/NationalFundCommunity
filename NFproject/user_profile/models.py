from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):

    PROFILE_TYPE_CHOICES = (
        ("I", "individual"),
        ("O", "orginization"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    website = models.URLField(blank=True)
    profile_type = models.CharField(max_length=1, choices=PROFILE_TYPE_CHOICES)

    def get_absolute_url(self):
        return reverse('profile', args=[self.user.username])

    def __str__(self):
        return self.user.username


class IndividualProfile(Profile):
    age = models.IntegerField()  # individual
    interest = models.CharField(max_length=200)  # individual


class OrginizationProfile (Profile):
    company_name = models.CharField(max_length=200)  # orginization
    location_URL = models.URLField()  # orgn


@receiver(pre_save, sender=Profile)
def add_slug_to_profile(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.user.username, allow_unicode=True)
