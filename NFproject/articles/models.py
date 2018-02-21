from django.db import models

# Create your models here.
class Article(models. Model):
    author= models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField()
    tags= models.CharField(max_length=20)
    content= models.TextField()
    picture = models.ImageField()

    def __str__(self):
        return self.title
