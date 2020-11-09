from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Логин', required=True)
    email = forms.EmailField(label='Почта', max_length=254, help_text='Это поле обязательно')
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (повторно)',
                                widget=forms.PasswordInput,
                                help_text='Введите пароль ещё раз')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
