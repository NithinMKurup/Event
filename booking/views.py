from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Booking
from .forms import Booking_form
from events.models import Events
import json
from django.db import transaction

# Helper function to restore tickets and delete booking
def restore_tickets_and_delete_booking(booking):
    event = get_object_or_404(Events, id=booking.name.id)
    with transaction.atomic():
        event.tickets_count += booking.no_of_tickets
        event.save()
        booking.delete()

# View for handling bookings
def booking(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    
    if request.method == 'POST':
        form = Booking_form(request.POST)
        if form.is_valid():
            booking_instance = form.save(commit=False)
            booking_instance.Cust_name = request.user.username
            
            # Check and update tickets count
            if event.tickets_count >= booking_instance.no_of_tickets:
                event.tickets_count -= booking_instance.no_of_tickets
                with transaction.atomic():
                    event.save()
                    booking_instance.save()
                messages.success(request, 'Booking successfully made.')
                return redirect('mybooking')
            else:
                messages.error(request, 'Not enough tickets available.')
    
    else:
        form = Booking_form()
    
    context = {
        'form': form,
        'event': event,
    }
    
    return render(request, 'booking.html', context)

# View for showing the user's bookings based on Cust_name
def my_bookings(request):
    bookings = Booking.objects.filter(Cust_name=request.user.username)
    messages_json = json.dumps([message.message for message in messages.get_messages(request)])
    context = {
        'bookings': bookings,
        'messages_json': messages_json
    }
    return render(request, 'mybooking.html', context)

# View for canceling a booking
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, Cust_name=request.user.username)

    if request.method == 'POST':
        restore_tickets_and_delete_booking(booking)
        messages.success(request, 'Booking successfully canceled.')
        return redirect('mybooking')
    
    return render(request, 'cancel_booking.html', {'booking': booking})

def superuser_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser)(view_func)
    return decorated_view_func

# View for managing bookings (accessible only by superusers)
@superuser_required
def manage_bookings(request):
    bookings = Booking.objects.all()

    # Handle delete request
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = get_object_or_404(Booking, id=booking_id)
        restore_tickets_and_delete_booking(booking)
        messages.success(request, 'Booking successfully deleted.')
        return redirect('manage_booking')

    context = {
        'bookings': bookings
    }
    return render(request, 'manage_booking.html', context)
