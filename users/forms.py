from django import forms
from django.contrib.auth.models import User
from users.models import Profile
from .models import Requirements  # Import the Requirements model

class userUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['bio']
        
class RequirementsForm(forms.ModelForm):
    class Meta:
        model = Requirements
        fields = ['name', 'email', 'phone_no', 'why']