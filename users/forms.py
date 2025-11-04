from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['first_name', 'last_name', 'email', 'mobile', 'membership_id', 'status', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter mobile number'
            }),
            'membership_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter membership ID'
            }),
            'status': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter status (e.g. Active)'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }),
        }
