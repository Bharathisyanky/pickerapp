from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    categories = models.ManyToManyField(Category)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name