from django.db import models

# Create your models here.
class Events(models.Model):
    organizer = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    event_type = models.TextField()
    content = models.TextField()
    location_url = models.URLField()
    location_name= models.CharField(max_length=400)
    picture = models.ImageField(upload_to='event_pictures', blank=True)

    def __str__(self):
        return self.title
