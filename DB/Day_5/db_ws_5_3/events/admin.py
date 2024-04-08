from django.contrib import admin

from .models import Participant, Event, Attendance
# Register your models here.
admin.site.register(Participant)
admin.site.register(Event)
admin.site.register(Attendance)