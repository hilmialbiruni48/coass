from django import http
from django.http import response
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from Daily_Journal.forms import JournalForm
from Daily_Journal.models import Journal
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='Authentication:login')
def journal_page(request):
    form = JournalForm()
    if request.is_ajax():
        form = JournalForm(request.POST)
        if form.is_valid():
            pick_user = request.user
            new_form = form.save(commit=False)
            new_form.user = pick_user
            new_form.save()
            return JsonResponse({
                'msg': 'Success'
            })
    return render(request, "index.html",{"form":form})

@login_required(login_url='Authentication:login')
def card_list(request):
    pick_user = request.user
    data = []

    try:
        data = Journal.objects.filter(user=pick_user)
       
    except:
        data = []
    return render(request, "card_list.html", {"jurnal":data})

@csrf_exempt
def card_list_flutter(request):
    # function buat flutter
    pick_user = request.user
    data = []

    try:
        data = Journal.objects.filter(user=pick_user)
       
    except:
        data = []
    dataa = serializers.serialize('json', data)
    return HttpResponse(dataa, content_type="application/json")

def json(request):
    journal = Journal.objects.all()
    data = serializers.serialize('json', journal)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def postMethod(request):
    #trigger
    print("***************************************************")
    # print(User.objects.get(username = "athif"))
    print("***************************************************")
    # if is_demam == "Ya": 
    #     is_demam = True
    # else:
    #     is_demam = False
    
    # if is_batuk == "Ya": 
    #     is_batuk = True
    # else:
    #     is_batuk = False

    # if is_kelelahan == "Ya": 
    #     is_kelelahan = True
    # else:
    #     is_kelelahan = False

    # if is_penciuman == "Ya": 
    #     is_penciuman = True
    # else:
    #     is_penciuman = False

    journal = Journal(
        hari = request.POST.get('hari', None),
        tanggal = request.POST.get('tanggal', None),
        is_demam = request.POST.get('is_demam', None),
        is_batuk = request.POST.get('is_batuk', None),
        is_kelelahan = request.POST.get('is_kelelahan', None),
        is_penciuman = request.POST.get('is_penciuman', None),
        curhat = request.POST.get('curhat', None),
        user = User.objects.get(username =request.POST.get('user', None)),
        # user = userr
    )
    journal.save()
    return JsonResponse({"status" : "berhasil"})