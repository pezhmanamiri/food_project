from django.urls import path
from .views import select_meals_view, summary_view, edit_meal_view, admin_report_view

urlpatterns = [
    path('select/', select_meals_view, name='select_meals'),
    path('summary/', summary_view, name='summary'),
    path('edit/<meal_date>/', edit_meal_view, name='edit_meal'),
    path('admin_report/', admin_report_view, name='admin_report'),

]
