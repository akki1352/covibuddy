from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from vaccination.models import VaccineType, VaccineCentre

def vaccineTypes(request):
    vaccineType = VaccineType.objects.all()
    vList = list(vaccineType.values())
    response = {}
    response['VaccineTypes'] = vList
    return JsonResponse(response, content_type='application/json')

def vaccineCentres(request):
    vaccineCentre = VaccineCentre.objects.all()
    vList = list(vaccineCentre.values())
    response = {}
    response['vaccineCentres'] = vList
    return JsonResponse(response, content_type='application/json')
