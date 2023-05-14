"""co_ass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# import Daily_Journal.urls as Daily_Journal
# import Authentication.urls as Authentication
# import Catatan_Kesehatan.urls as Catatan_Kesehatan
# import Reminder_Aktivitas.urls as Reminder_Aktivitas
# import Reminder_Makan_Minum.urls as Reminder_Makan_Minum
# import Reminder_Obat.urls as Reminder_Obat
# import Riwayat_SWAB.urls as Riwayat_SWAB

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('daily-journal/', include('Daily_Journal.urls')),
    path('authentication/', include('Authentication.urls')),
    path('health-records/', include('Catatan_Kesehatan.urls')),
    path('your-routine/', include('Reminder_Aktivitas.urls')),
    path('food-schedule/', include('Reminder_Makan_Minum.urls')),
    path('your-medicine/', include('Reminder_Obat.urls')),
    path('swab-records/', include('Riwayat_SWAB.urls')),
    
]
