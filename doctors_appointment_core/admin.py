from django.contrib import admin
from .models import *

# Register your models here.

class CancellationReasonsAdmin(admin.ModelAdmin):
  pass

admin.site.register(CancellationReason, CancellationReasonsAdmin)


class UserProfileAdmin(admin.ModelAdmin):
  pass

admin.site.register(UserProfile, UserProfileAdmin)


class EmergencyContactAdmin(admin.ModelAdmin):
  pass

admin.site.register(EmergencyContact, EmergencyContactAdmin)


class HealthFacilityAdmin(admin.ModelAdmin):
  pass

admin.site.register(HealthFacility, HealthFacilityAdmin)


class HealthFacilityHoursAdmin(admin.ModelAdmin):
  pass

admin.site.register(HealthFacilityHour, HealthFacilityHoursAdmin)


class SpecialistAdmin(admin.ModelAdmin):
  pass

admin.site.register(Specialist, SpecialistAdmin)


class SpecializationAdmin(admin.ModelAdmin):
  pass

admin.site.register(Specialization, SpecializationAdmin)


class AppointmentAdmin(admin.ModelAdmin):
  pass

admin.site.register(Appointment, AppointmentAdmin)


class AppointmentNotesAdmin(admin.ModelAdmin):
  pass

admin.site.register(AppointmentNote, AppointmentNotesAdmin)
