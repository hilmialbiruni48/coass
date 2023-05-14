from django.urls import path

from .views import  index, json, add_health_record, card_flutter


urlpatterns = [
    path('', index, name='index'),
    path('add', add_health_record , name='add_health_record'),
    path('json', json, name ='json'),
    path('card-flutter', card_flutter, name='card-flutter')

]