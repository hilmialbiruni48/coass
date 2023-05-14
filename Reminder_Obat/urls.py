from django.urls import path

from . import views

app_name = 'Reminder_Obat'

urlpatterns = [
    path('', views.list_medicine, name='list_medicine'),
    path('add-medicine', views.add_medicine, name='add_medicine'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('json', views.json, name='json'),
    # path('medicine-flutter', medicine_flutter, name='medicine-flutter')
]
