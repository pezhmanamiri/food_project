from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    personnel_code = models.CharField('کد پرسنلی', max_length=10, unique=True)
    password = models.CharField('رمز عبور', max_length=100)
    full_name = models.CharField('نام کامل', max_length=100, blank=True)

    def __str__(self):
        return f"{self.full_name or 'بدون نام'} - {self.personnel_code}"
