from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Employee


def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['personnel_code']
            password = form.cleaned_data['password']
            try:
                employee = Employee.objects.get(personnel_code=code, password=password)
                request.session['employee_id'] = employee.id
                return redirect('select_meals')  # این صفحه بعدی رو بعداً طراحی می‌کنیم
            except Employee.DoesNotExist:
                error_message = 'کد پرسنلی یا رمز عبور اشتباه است.'
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form, 'error_message': error_message})
