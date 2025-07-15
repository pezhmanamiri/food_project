from django.shortcuts import redirect
from django.urls import path
from .views import login_view

urlpatterns = [
    path('', lambda request: redirect('login'), name='home'),
    path('login/', login_view, name='login'),
]
