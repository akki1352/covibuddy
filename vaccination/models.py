from django.db import models

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