from django.db import models

# Create your models here.
class Events(models.Model):
    img=models.ImageField(upload_to='pic')
    name=models.CharField(max_length=50) 
    venue=models.CharField(max_length=50)
    Date=models.DateField()
    rate=models.IntegerField()
    tickets_count = models.PositiveIntegerField(default=0)
    Booking_Closes_on=models.DateField()
    def __str__(self):
        return self.name