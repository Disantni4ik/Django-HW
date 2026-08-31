from django import forms
from django.contrib.auth.models import User

from accounts.models import Profile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': "Ім'я",
            'last_name': 'Прізвище',
            'email': 'Пошта'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': "Введіть ваше ім'я"
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': "Введіть ваше прізвище"
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введіть вашу пошту',
            })
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birth_date', 'location', 'website']
        labels = {
            'avatar': "Аватар",
            'bio': 'Про себе',
            'birth_date': 'Дата народження',
            'location': 'Місто',
            'website': 'Веб-сторінка'
        }
        widgets = {
            'avatar': forms.FileInput(attrs={
                'class': 'form-input',
                'placeholder': "Завантажте ваш аватар"
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': "Введіть щось про себе"
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введіть вашу дату народження',
                'type': 'date'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введіть ваше місто',
            }),
            'website': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введіть сайт',
            })
        }