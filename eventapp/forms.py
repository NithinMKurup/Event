from django import forms
from .models import welcome_page

class WelcomePageForm(forms.ModelForm):
    class Meta:
        model = welcome_page
        fields = ['img', 'name', 'venue', 'date', 'description', 'count']

