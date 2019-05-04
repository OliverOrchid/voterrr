"""
Create your every model just here.
"""
from django.db import models

class  Musician(models.Model):
    first_name= models.CharField(max_length =50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)

    name = models.CharField(max_length = 100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Person(models.Model):
    SHIRT_SIZES = (
        ('s','small'),
        ('m','medium'),
        ('l','large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    