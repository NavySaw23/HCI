from django.db import models
from django.conf import settings

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    creator_linkedin = models.URLField()
    like_count = models.IntegerField(default=0)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to='img/projects')
    description = models.CharField(max_length=500, default="Lorem")