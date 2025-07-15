from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MealOption, EmployeeMealSelection

admin.site.register(MealOption)
admin.site.register(EmployeeMealSelection)
