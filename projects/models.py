from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    creator_linkedin = models.URLField()
    like_count = models.IntegerField(default=0)
    image = models.ImageField()