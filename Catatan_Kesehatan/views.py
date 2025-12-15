
from django import http
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from .models import *
from .forms import healthRecordForm
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required(login_url='Authentication:login')
def index(request):
    pick_user = request.user
    data = []

    try:
        data = healthRecord.objects.filter(user=pick_user)
       
    except:
        data = []
    return render(request, "informasi-kesehatan.html",{"health":data, "health":data})

@login_required(login_url='Authentication:login')
def json(request):
    health = healthRecord.objects.all().values()
    data = serializers.serialize('json', healthRecord.objects.all())
    return HttpResponse(data, content_type="application/json")

@login_required(login_url='Authentication:login')
def add_health_record(request):
    form = healthRecordForm()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = healthRecordForm(request.POST)
        if form.is_valid():
            pick_user = request.user
            new_form = form.save(commit=False)
            new_form.user = pick_user
            new_form.save()
            return JsonResponse({
                'msg': 'Success'
            })

    return render(request, 'add-health-record.html', {"form":form})



@csrf_exempt
def card_flutter(request):
    pick_user = request.user
    data = []

    try:
        data = healthRecord.objects.filter(user=pick_user)
       
    except:
        data = []
    dataa = serializers.serialize('json', data)
    return HttpResponse(dataa, content_type="application/json")