from django.db import models

# Create your models here.

class Types (models.Model):
    name = models.CharField(max_length=30)

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

    def __str__(self):
        return self.title
    
    def image_url (self):
        if self.picture and hasattr(self.picture , 'url'):
            return self.picture.url
        else:
            return "/static/img.png"
