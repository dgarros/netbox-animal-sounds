from django.db import models


class Animal(models.Model):
    """
    A database table representing animals and the sound each makes.
    """
    name = models.CharField(max_length=50)
    sound = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

