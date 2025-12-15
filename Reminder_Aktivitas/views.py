from django.core import serializers
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Activity, Event
from .forms import ActivityForm, EventForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required(login_url='Authentication:login')
def list_activity(request):
    pick_user = request.user
    data = []
    data2 = []

    try:
        data = Activity.objects.filter(user=pick_user)
        data2 = Event.objects.filter(user=pick_user)
       
    except:
        data = []
        data2 = []
    return render(request, 'list_activity_reminder.html', {"activities":data, "activities":data, "events":data2, "events":data2})

def json(request):
    activities = Activity.objects.all().values()
    data = serializers.serialize('json', Activity.objects.all())
    return HttpResponse(data, content_type="application/json")

@login_required(login_url='Authentication:login')
def add_activity(request):
    form = ActivityForm()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ActivityForm(request.POST)
        if form.is_valid():
            pick_user = request.user
            new_form = form.save(commit=False)
            new_form.user = pick_user
            new_form.save()
            return JsonResponse({
                'msg': 'Success'
            })

    return render(request, 'add_activity_reminder.html', {'form': form})

@login_required(login_url='Authentication:login')
def add_event(request):
    add_event = EventForm()
    if (request.method == "POST"):
        add_event = EventForm(request.POST)
        if (add_event.is_valid()):
            pick_user = request.user
            new_form = add_event.save(commit=False)
            new_form.user = pick_user
            new_form.save()
            
    response = {'add_event':add_event}
    return render(request, 'add_event_reminder.html', response)



