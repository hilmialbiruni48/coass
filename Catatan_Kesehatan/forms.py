from django import forms
from .models import healthRecord

class healthRecordForm(forms.ModelForm):
	class Meta:
		model = healthRecord
		fields = ["hari", "tanggal", "suhu", "sistolik", "diastolik", "jantung", "saturasi"]