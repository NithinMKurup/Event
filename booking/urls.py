from django.urls import path
from . import views

urlpatterns = [
    path('booking/<int:event_id>/', views.booking, name='booking'),
    path('mybooking',views.my_bookings,name='mybooking'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('manage_booking/', views.manage_bookings, name='manage_booking'),
    
]