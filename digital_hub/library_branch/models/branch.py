from django.db import models

from shcedule.models.calendars import CalendarManager
# Create your models here.

class Branch(models.Model, Calendarmanager):
    name = models.TextField()
