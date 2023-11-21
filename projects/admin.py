from django.contrib import admin

from .models import SDC_Project, PD_Project, AT_Project
# Register your models here.
admin.site.register(SDC_Project)
admin.site.register(PD_Project)
admin.site.register(AT_Project)