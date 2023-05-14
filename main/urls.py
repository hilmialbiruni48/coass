from django.urls import path

from main.views import home, json_funct, list_feedback, fetch_post_feedback

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('feedback', list_feedback, name='feedback'),
    path('json_function', json_funct, name='json_function'),
    path('fetch_feedback', fetch_post_feedback, name='fetch_feedback'),
]
