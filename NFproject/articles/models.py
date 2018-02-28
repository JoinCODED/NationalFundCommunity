from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=30)
    slug= models.SlugField(blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField()
    category = models.ManyToManyField(Category, related_name="categoriesOfArticles")
    content = models.TextField()
    picture = models.ImageField(upload_to='article_pictures', blank=True)
    slug= models.SlugField(blank=True)

    def __str__(self):
        return self.title

    def image_url (self):
        if self.picture and hasattr(self.picture , 'url'):
            return self.picture.url
        else:
            return "/static/img.png"

def create_slug (instance,Model,field_name,new_slug=None):
    slug=new_slug or slugify(getattr(instance,field_name))
    qs= Model.objects.filter(slug=slug).order_by('-id')
    if qs.exists():
        new_slug=f'{slug}-{qs.first().id}'
        return create_slug(instance, Model, field_name, new_slug=new_slug)
    return slug

@receiver (pre_save, sender= Category)
def add_slug_to_Category (sender, instance, **kwargs):
    if not instance.slug:
        instance.slug=create_slug(instance,sender,'name')


@receiver(pre_save, sender= Article)
def add_slug_to_Article(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug=create_slug(instance,sender,'title')
