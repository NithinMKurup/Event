from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Events 
from booking.models import Booking
from .forms import EventForm
from django.contrib import messages

MAX_TICKETS = 100000

@login_required
def events_view(request):
    events = Events.objects.all()

    if request.user.is_superuser:
        if request.method == 'POST':
            if 'add_event' in request.POST:
                form = EventForm(request.POST, request.FILES)
                if form.is_valid():
                    event = form.save(commit=False)
                    if event.tickets_count > MAX_TICKETS:
                        messages.error(request, f"The number of tickets cannot exceed {MAX_TICKETS}.")
                    else:
                        event.save()
                        return redirect('events')  # Adjust to the correct URL name

            elif 'modify_event' in request.POST:
                event_id = request.POST.get('event_id')
                event = get_object_or_404(Events, id=event_id)
                form = EventForm(request.POST, request.FILES, instance=event)
                if form.is_valid():
                    if form.cleaned_data['tickets_count'] > MAX_TICKETS:
                        messages.error(request, f"The number of tickets cannot exceed {MAX_TICKETS}.")
                    else:
                        form.save()
                        return redirect('admin_events')  # Adjust to the correct URL name

            elif 'delete_event' in request.POST:
                event_id = request.POST.get('event_id')
                event = get_object_or_404(Events, id=event_id)
                event.delete()
                return redirect('admin_events')  # Adjust to the correct URL name

        else:
            form = EventForm()

        context = {
            'events': events,
            'form': form,
        }
        return render(request, 'admin_events.html', context)
    
    else:
        context = {
            'events': events,
        }
        return render(request, 'events.html', context)

@login_required
def modify_event(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('admin_events')  # Adjust to the correct URL name
    else:
        form = EventForm(instance=event)
    return render(request, 'modify_event.html', {'form': form, 'event': event})

def home_view(request):
    events = Events.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'home.html', context)
