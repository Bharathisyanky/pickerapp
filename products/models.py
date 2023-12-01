from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    # Add other user-related fields

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add other order-related fields