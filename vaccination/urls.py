from django.urls import path

from . import views

urlpatterns = [
    path('vaccineTypes', views.vaccineTypes, name='vaccineTypes'),
    path('vaccineCentres', views.vaccineCentres, name='vaccineCentres')
]