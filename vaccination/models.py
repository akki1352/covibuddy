from django.db import models
import uuid
from covibuddy import settings

class VaccineType(models.Model):
    name = models.CharField(max_length=60)
    duration = models.IntegerField()
    stock = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return self.name

class VaccineCentre(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=40)
    stock = models.IntegerField()
    vaccineCost = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40, unique=True)
    password = models.CharField(max_length=20)
    contact = models.CharField(max_length=13)
    type = models.CharField(max_length=10)

    # def __str__(self):
    #     return self.name

class Volunteer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)

class Hospitals(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, unique=True)
    bedType = models.CharField(max_length=30)
    availability = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)

class Bookings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userId = models.UUIDField(default=uuid.uuid4, editable=False)
    hospitalId = models.UUIDField(default=uuid.uuid4, editable=False)
    bookingType = models.CharField(max_length=30)
    bookingDate = models.DateField()

class BookingsType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bookingType = models.CharField(max_length=30, unique=True)
    
class Suppliers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    supplyType = models.CharField(max_length=30)
    stock = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)

class CovidCentres(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=30)
    availability = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)

class Ambulances(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    fare = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)

class LabTest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    testType = models.CharField(max_length=30)
    cost = models.IntegerField()
    location = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)