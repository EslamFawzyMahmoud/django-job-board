from django.contrib import admin

# Register your models here.
from .models import Job ,Apply, Category

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Apply)