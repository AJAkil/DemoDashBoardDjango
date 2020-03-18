from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import DiseaseEntry


def index(request):
    return render(request, 'charts.html', {"Customer": 10})


def get_data(request):
    data = {
        "number_effected": list(DiseaseEntry.objects.all().values('number_effected')),
        "Countries": list(DiseaseEntry.objects.all().values('country_name')),
        "numbers_recovered": list(DiseaseEntry.objects.all().values('numbers_recovered')),
    }
    return JsonResponse(data)
