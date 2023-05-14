from django import forms
from .models import Activity, Event

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['date', 'aktivitas']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['tanggal', 'waktuawal', 'waktuakhir', 'event']