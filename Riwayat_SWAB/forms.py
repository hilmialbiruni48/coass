from django import forms
from Riwayat_SWAB.models import swabRecord

class SwabRecordsForm(forms.ModelForm):
    class Meta:
        model = swabRecord
        fields = ["tanggal", "hasil", "ctValue"]
    