from django.db import models

class Category(models.Model):

  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name

class Movie(models.Model):

  name = models.CharField(max_length=50)

  year = models.IntegerField()

  rating = models.IntegerField()

  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.name +" - "+str(self.year)