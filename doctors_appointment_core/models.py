from django.db import models
from django.contrib.auth.models import User
from .constants import APPOINTMENT_STATUSES, USER_PROFILE_TYPES

# Create your models here.


class UserProfile(models.Model):
  """Defines a custom user profile linked to the default User model"""
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  contact_number = models.CharField(max_length=16)
  profile_type = models.CharField(choices=USER_PROFILE_TYPES, max_length=13)

  def __str__(self) -> str:
    return "({id}) Profile: {user}".format(
      id=self.id,
      user=self.user.username
    )


class EmergencyContact(models.Model):
  """Defines an emergency contact for a related patient / user"""
  related_user = models.ForeignKey(User, on_delete=models.CASCADE)
  full_name = models.CharField(max_length=45)
  contact_number = models.CharField(max_length=16)
  email_address = models.EmailField()
  relationship_to_user = models.CharField(max_length=20)

  def __str__(self) -> str:
    return "({id}) Emergency Contact: {full_name}".format(
      id=self.id,
      full_name=self.full_name
    )

class HealthFacility(models.Model):
  """Defines a health facility where appointments are booked"""
  name = models.CharField(max_length=75)
  street_address_1 = models.CharField(max_length=200)
  street_address_2 = models.CharField(blank=True, max_length=200, null=True)
  region = models.CharField(max_length=25)
  contact_number = models.CharField(max_length=16)
  email_address = models.EmailField()

  class Meta:
    verbose_name_plural = 'Health Facilities'

  def __str__(self) -> str:
    return "({id}) Facility {name}".format(id=self.id, name=self.name)


class HealthFacilityHour(models.Model):
  """Defines open hours for a given facility"""
  related_facility = models.ForeignKey(HealthFacility, on_delete=models.CASCADE)
  day_from = models.CharField(max_length=8)
  time_from = models.TimeField()
  day_to = models.CharField(max_length=8)
  time_to = models.TimeField()

  def __str__(self) -> str:
    return "{facility} - {day}".format(
      facility=self.related_facility.name,
      day=self.day_from
    )

class Specialist(models.Model):
  """Defines a specialist or doctor"""
  full_name = models.CharField(max_length=70)
  related_facility = models.ForeignKey(HealthFacility, on_delete=models.CASCADE)
  date_started = models.DateField()

  def __str__(self) -> str:
    return "Specialist: {}".format(self.full_name)

class Specialization(models.Model):
  """Defines specializations for a given specialist / doctor"""
  related_specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
  name = models.CharField(max_length=20)
  description = models.TextField()

  def __str__(self) -> str:
    return "Specialization: {spec_name} for Specialist: {spec}".format(
      spec=self.related_specialist.full_name,
      spec_name=self.name
    )


class Appointment(models.Model):
  """Defines appointments that can be booked by patients(user)"""
  appointment_date = models.DateTimeField()
  status = models.CharField(choices=APPOINTMENT_STATUSES, max_length=12, default='booked')
  patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
  check_in_time = models.DateTimeField(blank=True, null=True)
  duration_minutes = models.PositiveSmallIntegerField(blank=False, null=True)
  cancelled_at = models.DateTimeField(blank=True, null=True)

  def __str__(self) -> str:
    return "Appointment: {id} for User: {user}".format(
      id=self.id,
      user=self.patient.user.username
    )


class AppointmentNote(models.Model):
  """Defines appointment notes for a given appointment"""
  related_appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
  note = models.TextField()

  def __str__(self) -> str:
    return "Note for Appointment: {appt_id}".format(
      appt_id=self.related_appointment.id,
    )


class CancellationReason(models.Model):
  """
  Preset appointment cancellation reasons with associated descriptive text
  ...
  Attributes
  -----------
  title : models.CharField
    The main text or title of the cancellation reason
  description : models.TextField
    Provides more detailed information about the reason for cancellation
  """
  title = models.CharField(max_length=75)
  description = models.TextField()

  def __str__(self) -> str:
    return "({id}) Cancellation Reason: {title}".format(
      id=self.id,
      title=self.title
    )

