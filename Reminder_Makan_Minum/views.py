from django import http
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from .models import *
from .forms import makanMinumForm
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='Authentication:login')
def index(request):
    pick_user = request.user
    data=[]
    try:
        data = makanMinum.objects.filter(user=pick_user)
    
    except:
        data=[]

    return render(request, "informasi-makan-minum.html",{"minumMakan":data, "minumMakan":data})

@login_required(login_url='Authentication:login')
def json(request):
    minumMakan = makanMinum.objects.all().values()
    data = serializers.serialize('json', makanMinum.objects.all())
    return HttpResponse(data, content_type="application/json")

@login_required(login_url='Authentication:login')
def add_makan_minum(request):
    form = makanMinumForm()
    if request.is_ajax():
        form = makanMinumForm(request.POST)
        if form.is_valid():
            # form.save()
            pick_user = request.user
            new_form = form.save(commit=False)
            new_form.user = pick_user
            new_form.save()
            return JsonResponse({
                'msg': 'Success'
            })

    return render(request, 'add-makan-minum.html', {"form":form})

