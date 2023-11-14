from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    username = models.CharField(max_length=100)
    Hasliked = ArrayField(models.BooleanField())    