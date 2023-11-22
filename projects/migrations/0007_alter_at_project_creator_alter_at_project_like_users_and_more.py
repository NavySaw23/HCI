# Generated by Django 4.2 on 2023-11-21 07:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0006_at_project_pd_project_sdc_project_delete_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='at_project',
            name='creator',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='at_project',
            name='like_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pd_project',
            name='creator',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pd_project',
            name='like_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sdc_project',
            name='creator',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sdc_project',
            name='like_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]