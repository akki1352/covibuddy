from django.db import models
import uuid
from covibuddy import settings

class Users(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=40, unique=True)
    password = models.CharField(max_length=20)
    contact = models.CharField(max_length=13)
    type = models.CharField(max_length=10)
    location = models.CharField(max_length=30)

    # def __str__(self):
    #     return self.name

class Volunteer(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)

class Hospitals(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=40, unique=True)
    bedType = models.CharField(max_length=30)
    availability = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)

class Bookings(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    userId = models.IntegerField(editable=False)
    hospitalId = models.IntegerField(default=int, editable=False)
    bookingType = models.CharField(max_length=30)
    bookingDate = models.DateField()

class BookingsType(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    bookingType = models.CharField(max_length=30, unique=True)
    
class Suppliers(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=40)
    supplyType = models.CharField(max_length=30)
    stock = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)

class CovidCareCentres(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=30)
    availability = models.IntegerField(default=int)
    location = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)

class CovidTestingLabs(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=40)
    testType = models.CharField(max_length=30)
    cost = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)

class Ambulances(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=40)
    fare = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)