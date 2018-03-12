from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, m2m_changed
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Types(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name


class Events(models.Model):
    organizer = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    event_type = models.ForeignKey(Types, blank=True, null=True,
                                   on_delete=models.SET_NULL,
                                   related_name='belongsTo')
    content = models.TextField()
    location_url = models.URLField()
    location_name = models.CharField(max_length=400)
    picture = models.ImageField(upload_to='event_pictures', blank=True)
    attendees = models.ManyToManyField(User, related_name="events", blank=True)
    slug = models.SlugField(blank=True)
    maximum_attendees = models.PositiveIntegerField()
    seats_taken = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events:event', args=[self.slug])

    def image_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url
        else:
            return "/static/img.png"

    class Meta:
        ordering = ['-date']


def create_slug(instance, Model, field_name, new_slug=None):
    slug = new_slug or slugify(getattr(instance, field_name),
                               allow_unicode=True)
    qs = Model.objects.filter(slug=slug).order_by('-id')
    if qs.exists():
        new_slug = f'{slug}-{qs.first().id}'
        return create_slug(instance, Model, field_name, new_slug=new_slug)
    return slug

@receiver(m2m_changed, sender=Events.attendees.through)
def update_seats_taken(sender, instance, **kwargs):
    instance.seats_taken = instance.attendees.all().count()
    instance.save()

@receiver(pre_save, sender=Types)
def add_slug_to_Types(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance, sender, 'name')


@receiver(pre_save, sender=Events)
def add_slug_to_Events(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance, sender, 'title')
