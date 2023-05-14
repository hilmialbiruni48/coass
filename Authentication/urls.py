from django.urls import path

from . import views


app_name = 'Authentication' #Beda

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('sign-up/', views.signupPage, name='register'),
    path('log-out/', views.logoutUser, name='logout'),
    path('login-flutter/', views.login_with_flutter, name='login-flutter'),
    path('logout-flutter/', views.logout_with_flutter, name='logout-flutter'),
    # path('logout/', views.logoutUser, name="logout"),
    # path('', views.autentikasi, name='autentikasi'),
]
