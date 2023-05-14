from django import forms
from .models import Medicine 

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['hari', 'due_time', 'obat']