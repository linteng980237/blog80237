from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=128, unique=True)
    author = models.CharField(max_length=128)
    publisher = models.CharField(max_length=128)
    time = models.DateField()
    version = models.CharField(max_length=128)
    price = models.IntegerField
    
    def __str__(self):
        return self.title