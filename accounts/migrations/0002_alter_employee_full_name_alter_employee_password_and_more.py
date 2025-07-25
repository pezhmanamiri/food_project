# Generated by Django 5.2.4 on 2025-07-14 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='نام کامل'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=100, verbose_name='رمز عبور'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='personnel_code',
            field=models.CharField(max_length=10, unique=True, verbose_name='کد پرسنلی'),
        ),
    ]
