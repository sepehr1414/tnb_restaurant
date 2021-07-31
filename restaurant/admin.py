from django.contrib import admin
from . import models

admin.site.register(models.Restaurant)
admin.site.register(models.Food)
admin,admin.site.register(models.Comment)