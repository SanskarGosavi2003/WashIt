from asyncio.windows_events import NULL
from xml.dom import ValidationErr
from django.db import models

# Create your models here.
class WashingMachine(models.Model):
    floor = models.PositiveSmallIntegerField()
    wing = models.PositiveSmallIntegerField()
    occupy = models.TextField(max_length=99)
    occupied_at = models.DateTimeField(default =  None)
    occupied_till = models.DateTimeField(default = None)
    occupation_status = models.BooleanField(default= False, blank= True)

class Student(models.Model):
    floor = models.PositiveSmallIntegerField()
    wing = models.PositiveSmallIntegerField()
    time_alloted = models.DateTimeField(null=True,blank=True)
    m_floor = models.PositiveSmallIntegerField(default=NULL,blank=True)
    m_wing = models.PositiveSmallIntegerField(default=NULL,blank=True)
    I = models.CharField(max_length=9, default="")
    Linear_Rank = models.IntegerField(default=0,blank=True)