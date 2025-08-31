from django import forms
from .models import *

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['Name','Age','Gender','Height','Weight']