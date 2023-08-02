from django import forms
from .models import Event 
from django.contrib.auth.models import User



# Create your forms here.
class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('event_title', 'event_date','location','image')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
  
    class Meta:
        model = User 
        fields = ('username','email','password')

    
