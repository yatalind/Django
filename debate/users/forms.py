from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Not

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        
class NotEkleForm(forms.ModelForm):
    class Meta:
        model = Not
        fields = ['baslik', 'icerik']        