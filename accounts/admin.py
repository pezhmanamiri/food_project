from django.contrib import admin

# Register your models here.

from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('personnel_code', 'full_name')
    search_fields = ('personnel_code', 'full_name')
