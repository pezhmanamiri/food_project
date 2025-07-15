from django.db import models

# Create your models here.
from django.db import models
from datetime import date

class MealOption(models.Model):
    DAY_CHOICES = [
        ('0', 'شنبه'), ('1', 'یکشنبه'), ('2', 'دوشنبه'),
        ('3', 'سه‌شنبه'), ('4', 'چهارشنبه'), ('5', 'پنجشنبه'), ('6', 'جمعه'),
    ]
    MEAL_TYPES = [('breakfast', 'صبحانه'), ('lunch', 'ناهار'), ('dinner', 'شام')]

    day_of_week = models.CharField(max_length=1, choices=DAY_CHOICES)
    meal_type = models.CharField(max_length=10, choices=MEAL_TYPES)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.get_day_of_week_display()} - {self.get_meal_type_display()} - {self.name}"

class EmployeeMealSelection(models.Model):
    employee = models.ForeignKey('accounts.Employee', on_delete=models.CASCADE)
    date = models.DateField()
    breakfast = models.CharField(max_length=100, blank=True)
    lunch = models.CharField(max_length=100, blank=True)
    dinner = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.date}"
