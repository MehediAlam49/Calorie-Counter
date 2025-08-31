from django import forms
from .models import *

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['Name','Age','Gender','Height','Weight']

        widgets = {
            'Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'Age': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 120,
                'placeholder': 'Age in years'
            }),
            'Gender': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Height': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.1',
                'placeholder': 'Height in cm'
            }),
            'Weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.1',
                'placeholder': 'Weight in kg'
            }),
        }
