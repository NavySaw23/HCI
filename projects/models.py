from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    creator_linkedin = models.URLField()
    like_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='img/projects')
    description = models.CharField(max_length=500, default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatum debitis reprehenderit et blanditiis quam ex molestiae culpa, eius dolorem voluptate? Incidunt nostrum natus ut. Dicta, voluptas quam labore dolorum eius cum quisquam qui numquam quae?")