from graphene_django import DjangoObjectType

from doctors_appointment_core.models import *


class AppointmentType(DjangoObjectType):
  class Meta:
    model = Appointment
    fields = "__all__"


class AppointmentNoteType(DjangoObjectType):
  class Meta:
    model = AppointmentNote
    fields = "__all__"


class CancellationReasonType(DjangoObjectType):
  class Meta:
    model = CancellationReason
    fields = "__all__"


class EmergencyContactType(DjangoObjectType):
  class Meta:
    model = EmergencyContact
    fields = "__all__"


class HealthFacilityType(DjangoObjectType):
  class Meta:
    model = HealthFacility
    fields = "__all__"


class HealthFacilityHourType(DjangoObjectType):
  class Meta:
    model = HealthFacilityHour
    fields = "__all__"


class SpecialistType(DjangoObjectType):
  class Meta:
    model = Specialist
    fields = "__all__"


class SpecializationType(DjangoObjectType):
  class Meta:
    model = Specialization
    fields = "__all__"


class UserProfileType(DjangoObjectType):
  class Meta:
    model = UserProfile
    fields = "__all__"


class UserType(DjangoObjectType):
  class Meta:
    model = User
    fields = ("id", "email", "username")
