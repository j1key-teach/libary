from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    photo = models.ImageField(upload_to='photos/')
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name
