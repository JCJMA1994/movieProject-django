from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=70)
    date_birth = models.DateField()
    date_death = models.DateField(null=True, blank=True)
    biography = models.TextField()

    def __str__(self):
        return self.name + " " + self.lastname


class Movie(models.Model):
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    synopsis = models.TextField()
    duration = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()


    def __str__(self):
        return self.name