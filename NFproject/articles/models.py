from django.db import models

# Create your models here.
class Article(models. Model):
    Author= models.CharField(max_length =20)
    Title = models.CharField(max_length=30)
    Date_created = models.DateTimeField(auto_now_add=True)
    Featured = models.BooleanField()
    Tags= models.CharField(max_length= 20)
    content= models.TextField()
    pic = models.ImageField()

    def __str__(self):
        return self.Title
