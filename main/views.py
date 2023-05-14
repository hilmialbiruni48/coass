from django.shortcuts import render, redirect
from main.models import Feedback
from main.forms import FormFeedback
from django.http import HttpResponseRedirect, response, JsonResponse
import json
from django.core import serializers
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    form = FormFeedback()
    if request.is_ajax():
        form = FormFeedback(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'msg': 'Success'
            })
    return render(request, "main/home.html", {"form": form})


def list_feedback(request):
    feedback = Feedback.objects.all().values()
    response = {'feedback': feedback}
    return render(request, "main/form_feedback.html", response)


def json_funct(request):
    feedback = Feedback.objects.all()
    jsonFeedback = serializers.serialize('json', feedback)
    return HttpResponse(jsonFeedback, content_type="application/json")

@csrf_exempt
def fetch_post_feedback(request):
    print(request.method)
    print(request.body)
    data = json.loads(request.body)
    form = Feedback()
    form.name = data["username"]
    form.message = data["message"]
    form.save()
    return JsonResponse({"status" : "berhasil"})
