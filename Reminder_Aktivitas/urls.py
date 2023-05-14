from django.urls import path

from .views import add_activity, add_event, list_activity, json

urlpatterns = [
    path('', list_activity, name='list_activity'),
    path('json', json, name ='json'),
    path('add-activity', add_activity, name='add_activity'),
    path('add-event', add_event, name='add_event'),
]