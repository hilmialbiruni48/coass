from django import forms
from django.db.models.base import Model
from django.forms import fields
from Daily_Journal.models import Journal

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ["hari", "tanggal", "is_demam",  "is_batuk" ,"is_kelelahan", "is_penciuman", "curhat" ]