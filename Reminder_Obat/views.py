from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import Medicine
from .forms import MedicineForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required(login_url='Authentication:login')
def add_medicine(request):
    form = MedicineForm()
    if request.is_ajax():
        form = MedicineForm(request.POST)
        if form.is_valid():
            pick_user = request.user
            new_form = form.save(commit=False)
            new_form.user = pick_user
            new_form.save()
            return JsonResponse({
                'msg': 'Success'
            })
            
    return render(request, "reminder-add-obat.html", {"medicine":form})

@login_required(login_url='Authentication:login')
def list_medicine(request):
    pick_user = request.user
    data = []
    try:
        data = Medicine.objects.filter(user=pick_user)
       
    except:
        data = []

    return render(request, 'reminder-obat.html', {"medicine":data})

@csrf_exempt
def medicine_flutter(request):
    pick_user = request.user
    data = []

    try:
        data = Medicine.objects.filter(user=pick_user)
       
    except:
        data = []
    data_on = serializers.serialize('json', data)
    return HttpResponse(data_on, content_type="application/json")

@login_required(login_url='Authentication:login')
def delete(request, list_id):
    item = Medicine.objects.get(pk=list_id)
    item.delete()
    return redirect("/your-medicine/")

@login_required(login_url='Authentication:login')
def json(request):
    obat = Medicine.objects.all()
    jsonMedicine = serializers.serialize('json', obat)
    return HttpResponse(jsonMedicine, content_type="application/json")

