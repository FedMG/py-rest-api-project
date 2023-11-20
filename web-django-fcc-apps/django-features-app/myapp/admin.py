from django.contrib import admin
from .models import Feature

# Register your models here.
# to be reflected on the db and the admin panel dashboard
admin.site.register(Feature)