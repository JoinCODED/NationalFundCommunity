from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, allow_unicode=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               blank=True, null=True,
                               related_name='articlesOfUser')
    author_name = models.CharField(max_length=225, blank=True)
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    category = models.ManyToManyField(
        Category, related_name="categoriesOfArticles")
    content = models.TextField()
    picture = models.ImageField(upload_to='article_pictures', blank=True)
    slug = models.SlugField(blank=True, allow_unicode=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', args=[self.slug])

    def image_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url
        else:
            return "/static/img.png"


def create_slug(instance, Model, field_name, new_slug=None):
    slug = new_slug or slugify(
        getattr(instance, field_name), allow_unicode=True)
    qs = Model.objects.filter(slug=slug).order_by('-id')
    if qs.exists():
        new_slug = f'{slug}-{qs.first().id}'
        return create_slug(instance, Model, field_name, new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Category)
def add_slug_to_Category(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance, sender, 'name')


@receiver(pre_save, sender=Article)
def add_slug_to_Article(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance, sender, 'title')


@receiver(pre_save, sender=Article)
def add_author_name_to_article(sender, instance, **kwargs):
    author_name = "staff"
    author = instance.author
    if author:
        author_name = author.name()
    instance.author_name = author_name
