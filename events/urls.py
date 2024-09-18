from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('events/', views.events_view, name='events'),
    path('events/<int:event_id>/modify/', views.modify_event, name='modify_event'),
    path('admin_events/', views.events_view, name='admin_events'),  # Use the same view for admin
]


