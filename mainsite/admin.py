from django.contrib import admin
from mainsite import models

# Register your models here.
admin.site.register(models.Maker)
admin.site.register(models.PModel)
admin.site.register(models.Product)
admin.site.register(models.PPhoto)
