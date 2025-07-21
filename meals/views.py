from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from datetime import timedelta, date
from .models import MealOption, EmployeeMealSelection
from accounts.models import Employee

def select_meals_view(request):
    employee_id = request.session.get('employee_id')
    if not employee_id:
        return redirect('login')

    employee = Employee.objects.get(id=employee_id)
    today = date.today()
    days = [today + timedelta(days=i) for i in range(1, 8)]  # امروز تا هفت روز بعد

    if request.method == 'POST':
        for day in days:
            date_str = day.strftime('%Y-%m-%d')  # تبدیل date به string قابل استفاده در name=""
            breakfast = request.POST.get(f"breakfast_{date_str}")
            lunch = request.POST.get(f"lunch_{date_str}")
            dinner = request.POST.get(f"dinner_{date_str}")

            selection, _ = EmployeeMealSelection.objects.get_or_create(
                employee=employee,
                date=day
            )
            selection.breakfast = breakfast or ''
            selection.lunch = lunch or ''
            selection.dinner = dinner or ''
            selection.save()
        return redirect('summary')

    meal_options = {}

    for d in days:
        weekday = str((d.weekday() + 2) % 7)
        meal_options[d] = {
            'breakfast': MealOption.objects.filter(day_of_week=weekday, meal_type='breakfast'),
            'lunch': MealOption.objects.filter(day_of_week=weekday, meal_type='lunch'),
            'dinner': MealOption.objects.filter(day_of_week=weekday, meal_type='dinner'),
        }

    return render(request, 'meals/select_meals.html', {
        'employee': employee,
        'days': days,
        'meal_options': meal_options,
    })





from .models import EmployeeMealSelection
from datetime import date, timedelta

def summary_view(request):
    employee_id = request.session.get('employee_id')
    if not employee_id:
        return redirect('login')

    employee = Employee.objects.get(id=employee_id)
    today = date.today()
    days = [today + timedelta(days=i) for i in range(1, 8)]

    selections = EmployeeMealSelection.objects.filter(employee=employee, date__in=days).order_by('date')

    return render(request, 'meals/summary.html', {
        'employee': employee,
        'selections': selections,
    })









from django.utils.dateparse import parse_date
from django.http import Http404

def edit_meal_view(request, meal_date):
    employee_id = request.session.get('employee_id')
    if not employee_id:
        return redirect('login')

    try:
        target_date = parse_date(meal_date)
        if not target_date:
            raise ValueError
    except ValueError:
        raise Http404("تاریخ نامعتبر است")

    employee = Employee.objects.get(id=employee_id)

    selection, created = EmployeeMealSelection.objects.get_or_create(employee=employee, date=target_date)

    weekday = str((target_date.weekday() + 2) % 7)
    meal_options = {
        'breakfast': MealOption.objects.filter(day_of_week=weekday, meal_type='breakfast'),
        'lunch': MealOption.objects.filter(day_of_week=weekday, meal_type='lunch'),
        'dinner': MealOption.objects.filter(day_of_week=weekday, meal_type='dinner'),
    }

    if request.method == 'POST':
        selection.breakfast = request.POST.get('breakfast', '')
        selection.lunch = request.POST.get('lunch', '')
        selection.dinner = request.POST.get('dinner', '')
        selection.save()
        return redirect('summary')

    return render(request, 'meals/edit_meal.html', {
        'employee': employee,
        'date': target_date,
        'selection': selection,
        'meal_options': meal_options,
    })







from collections import defaultdict
from .models import EmployeeMealSelection
from datetime import date, timedelta

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_report_view(request):
    today = date.today()
    days = [today + timedelta(days=i) for i in range(1, 8)]

    report_data = {}

    for d in days:
        selections = EmployeeMealSelection.objects.filter(date=d).select_related('employee')
        day_data = {
            'breakfast': [],
            'lunch': [],
            'dinner': []
        }
        for s in selections:
            if s.breakfast:
                day_data['breakfast'].append((s.employee.full_name, s.breakfast))
            if s.lunch:
                day_data['lunch'].append((s.employee.full_name, s.lunch))
            if s.dinner:
                day_data['dinner'].append((s.employee.full_name, s.dinner))
        report_data[d] = day_data

    return render(request, 'meals/admin_report.html', {
        'days': days,
        'report_data': report_data
    })
