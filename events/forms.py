from django import forms
from .models import Events
import datetime

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['img', 'name', 'venue', 'Date', 'rate', 'Booking_Closes_on', 'tickets_count']
        widgets = {
            'Date': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'form-control',
                'min': datetime.date.today().strftime('%Y-%m-%d')
            }),
            'Booking_Closes_on': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'form-control',
                'min': datetime.date.today().strftime('%Y-%m-%d')
            }),
        }