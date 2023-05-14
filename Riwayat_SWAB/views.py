from django.http import response
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.http.response import HttpResponse
from .models import swabRecord
from .forms import SwabRecordsForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='Authentication:login')
def json(request):
    swab = swabRecord.objects.all().values()
    data = serializers.serialize('json', swabRecord.objects.all())
    return HttpResponse(data, content_type="application/json")

@login_required(login_url='Authentication:login')
def add_SWABRecords(request):
    form = SwabRecordsForm()
    if request.is_ajax():
        form = SwabRecordsForm(request.POST)
        if form.is_valid():
            pick_user = request.user
            new_form = form.save(commit=False)
            new_form.user = pick_user
            new_form.save()
            return JsonResponse({
                'msg':'Success'
            })
    
    return render(request, "add_riwayat_swab.html", {"form":form})

@login_required(login_url='Authentication:login')
def SWAB_records(request):
    # swab = swabRecord.objects.all().values()
    pick_user = request.user
    data = []

    try:
        data = swabRecord.objects.filter(user=pick_user)
       
    except:
        data = []
    return render(request, 'riwayat_swab.html', {"swab": data, "swab": data})