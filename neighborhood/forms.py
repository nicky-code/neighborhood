from .models import Profile,Business
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user']

