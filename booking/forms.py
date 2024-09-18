from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type='date'

    
class Booking_form(forms.ModelForm):
    class Meta:
        model=Booking
        fields= ('Cust_phno','name','no_of_tickets')

        widgets={
            'booking_date':DateInput(),
        }

        labels={
            'Cust_name':'Customer Name',
            'Cust_phno' : 'Mobile Number',
            'name': 'Event Name',
            'booking_date': 'Booking Date',
            'no_of_tickets': 'Ticket Count',
            'rate': 'Ticket rate',

        }