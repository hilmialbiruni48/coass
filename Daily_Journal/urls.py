from django.urls import path
from Daily_Journal.views import card_list, card_list_flutter, journal_page, json, postMethod

urlpatterns = [
    path('', card_list, name='journal_page'),
    path('tambah-jurnal', journal_page, name='add_journal'),
    path('json', json, name='json'),
    path('card-flutter', card_list_flutter, name='card-flutter'),
    path('post-flutter', postMethod, name='post-flutter'),

]