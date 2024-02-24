from django.db import models
import datetime


class Post(models.Model):
    # Corregí el typo en 'tittle' a 'title'
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    # Corregí aquí también
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title
