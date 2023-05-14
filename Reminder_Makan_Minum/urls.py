from django.urls import path

from .views import index, json, add_makan_minum


urlpatterns = [
    path('', index, name='index'),
    path('add', add_makan_minum, name='add_makan_minum'),
    path('json', json, name ='json')
]