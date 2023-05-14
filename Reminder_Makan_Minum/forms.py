from django import forms
from .models import makanMinum

class makanMinumForm(forms.ModelForm):
	class Meta:
		model = makanMinum
		fields = ["tanggal", "jadwalMakan", "makan", "minum"]