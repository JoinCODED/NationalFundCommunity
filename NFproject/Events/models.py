from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.

class Types (models.Model):
    name = models.CharField(max_length=30)
    slug= models.SlugField(blank=True, unique =True)

    def __str__(self):
        return self.name

class Events(models.Model):
    organizer = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    event_type = models.ForeignKey(
        Types, blank=True, null=True,
        on_delete=models.SET_NULL, related_name='belongsTo')
    content = models.TextField()
    location_url = models.URLField()
    location_name= models.CharField(max_length=400)
    picture = models.ImageField(upload_to='event_pictures', blank=True)
    slug= models.SlugField(blank=True, unique =True)

    def __str__(self):
        return self.title

    def image_url (self):
        if self.picture and hasattr(self.picture , 'url'):
            return self.picture.url
        else:
            return "/static/img.png"
    class Meta:
        ordering=['-date']

def create_slug (instance,Model,field_name,new_slug=None):
    slug=new_slug or slugify(getattr(instance,field_name))
    qs= Model.objects.filter(slug=slug).order_by('-id')
    if qs.exists():
        new_slug=f'{slug}-{qs.first().id}'
        return create_slug(instance, Model, field_name, new_slug=new_slug)
    return slug

@receiver (pre_save, sender= Types)
def add_slug_to_Types (sender, instance, **kwargs):
    if not instance.slug:
        instance.slug=create_slug(instance,sender,'name')


@receiver(pre_save, sender= Events)
def add_slug_to_Events(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug=create_slug(instance,sender,'title')
