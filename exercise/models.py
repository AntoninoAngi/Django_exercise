from django.db import models

class Car(models.Model):
    model_year = models.IntegerField()
    make = models.CharField(max_length=120)
    model = models.TextField()
    rejection_percentage = models.CharField(max_length=3) #DecimalField does not work since the json format is with the "comma" and not with the dot
    reason_1 = models.TextField(blank=True, null=True)
    reason_2 = models.TextField(blank=True, null=True)
    reason_3 = models.TextField(blank=True, null=True)