from django.contrib import admin
from mptt.admin import MPTTModelAdmin
# Register your models here.
from .models import Employee

admin.site.register(Employee)
