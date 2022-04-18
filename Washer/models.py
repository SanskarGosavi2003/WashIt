from xml.dom import ValidationErr
from django.db import models

# Create your models here.
class WashingMachine(models.Model):
    floor = models.PositiveSmallIntegerField()
    wing = models.PositiveSmallIntegerField()
    occupy = models.TextField(max_length=99)
    occupied_at = models.TimeField(default =  None)

class Student(models.Model):
    floor = models.PositiveSmallIntegerField()
    wing = models.PositiveSmallIntegerField()
    time_alloted = models.TimeField(default= None)
    m_floor = models.PositiveSmallIntegerField()
    m_wing = models.PositiveSmallIntegerField()
    I = models.CharField(max_length=9, default="")