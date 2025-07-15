from django import forms

class LoginForm(forms.Form):
    personnel_code = forms.CharField(label='کد پرسنلی', max_length=10)
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
