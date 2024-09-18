from django.db import models
from events.models import Events
import datetime

class Booking(models.Model):
    Cust_name = models.CharField(max_length=25)
    Cust_phno = models.CharField(max_length=12)
    name = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_bookings')
    booking_date = models.DateField(default=datetime.date.today)
    booked_on = models.DateField(auto_now=True)
    no_of_tickets = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.Cust_name} - {self.name.name}"