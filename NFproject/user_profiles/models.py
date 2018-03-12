from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse


class User(AbstractUser):
    is_individual = models.BooleanField('individual status', default=False)
    is_organization = models.BooleanField('organization status', default=False)

    def name(self):
        if self.is_individual:
            return self.individual.full_name()
        elif self.is_organization:
            return self.organization.company_name
        else:
            return 'Staff'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    website = models.URLField(blank=True)

    def save(self,*args , **kwargs):
        print("Before if")
        if self.user.is_individual != self.user.is_organization:
            print("inside if")
            raise ValidationError("Must be either individual or organization")
        super(Profile,self).save(*args , **kwargs)

    def get_absolute_url(self):
        return reverse('profiles:profile', args=[self.user.username])

    def __str__(self):
        return self.user.username

    class Meta:
        abstract = True


class Individual(Profile):
    age = models.IntegerField()  # individual
    interest = models.CharField(max_length=200)  # individual
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Organization(Profile):
    company_name = models.CharField(max_length=200)  # organization
    location_URL = models.URLField()  # orgn


@receiver(pre_save)
def add_slug_to_profile(sender, instance, **kwargs):
    if not issubclass(sender, Profile):
        return
    if not instance.slug:
        instance.slug = slugify(instance.user.username, allow_unicode=True)


@receiver(post_save)
def update_author_names(sender, instance, **kwargs):
    if not issubclass(sender, Profile):
        return
    article_list = instance.user.articlesOfUser.all()
    for article in article_list:
        article.save()

@receiver(post_save)
def set_user_type(sender,instance , **kwargs):
    if not issubclass(sender, Profile):
        return
    if isinstance(instance,Individual):
        instance.user.is_individual = True
    else:
        instance.user.is_organization= True
    instance.user.save()