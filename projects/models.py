from django.db import models
from django.conf import settings

# Create your models here.
# class Project(models.Model):
#     title = models.CharField(max_length=100)
#     creator = models.CharField(max_length=100)
#     creator_linkedin = models.URLField()
#     like_count = models.IntegerField(default=0)
#     like = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True)
#     image = models.ImageField(upload_to='img/projects')
#     description = models.CharField(max_length=500, default="Lorem")

class SDC_Project(models.Model):
    title = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    like_count = models.IntegerField(default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True)
    image = models.ImageField(upload_to='img/projects')
    description = models.CharField(max_length=500, default="Lorem")

class PD_Project(models.Model):
    title = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    like_count = models.IntegerField(default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True)
    image = models.ImageField(upload_to='img/projects')
    description = models.CharField(max_length=500, default="Lorem")

class AT_Project(models.Model):
    title = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    like_count = models.IntegerField(default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True)
    image = models.ImageField(upload_to='img/projects')
    description = models.CharField(max_length=500, default="Lorem")