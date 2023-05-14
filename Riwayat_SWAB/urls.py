from django.urls import path
from .views import add_SWABRecords, SWAB_records, json

urlpatterns = [
    path('', SWAB_records, name='SWAB_records'),
    path('add', add_SWABRecords, name='add_SWABrecords'),
    path('json', json, name ='json')
]