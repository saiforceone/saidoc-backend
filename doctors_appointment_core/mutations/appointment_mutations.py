import datetime
import graphene
from graphene_django import DjangoObjectType

from doctors_appointment_core.models import Appointment, Specialist, UserProfile

class AppointmentType(DjangoObjectType):
  class Meta:
    model = Appointment
    fields = "__all__"


class AppointmentMutation(graphene.Mutation):
  class Arguments:
    appointment_date = graphene.DateTime()
    specialist = graphene.String()
  
  success = graphene.Boolean()
  appointment = graphene.Field(AppointmentType)

  @classmethod
  def mutate(cls, root, info, **kwargs):

    if not info.context.user.is_authenticated:
      return None

    specialist_id = kwargs.pop('specialist')

    specialist_instance = Specialist.objects.get(pk=specialist_id)

    if not specialist_instance:
      return None

    user_profile = UserProfile.objects.get(user=info.context.user)

    appointment = Appointment(**kwargs)
    appointment.patient = user_profile
    appointment.specialist = specialist_instance
    appointment.status = 'booked'
    appointment.duration_minutes = 30

    appointment.save()
    success = True

    return AppointmentMutation(
      appointment=appointment,
      success=success
    )


class AppointmentUpdateMutation(graphene.Mutation):
  class Arguments:
    id = graphene.ID()
    status = graphene.String(required=False)
    check_in_date_time = graphene.DateTime(required=False)

  success = graphene.Boolean()
  appointment = graphene.Field(AppointmentType)

  @classmethod
  def mutate(cls, root, info, **kwargs):

    if not info.context.user.is_superuser:
      return None

    pk = kwargs.pop('id')

    if pk is None:
      return None

    appointment = Appointment.objects.get(pk=pk)

    check_in_date_time = kwargs.pop('check_in_date_time')

    # TODO: validate that check-in time comes after the appointment date/time

    for key, value in kwargs.items():
      setattr(appointment, key, value)

    if check_in_date_time is not None:
      appointment.status = 'in-progress'
      appointment.check_in_time = check_in_date_time

    appointment.save()
    success = True

    return AppointmentUpdateMutation(
      appointment=appointment,
      success=success
    )


class AppointmentCancellationMutation(graphene.Mutation):
  class Arguments:
    id = graphene.ID()

  success = graphene.Boolean()
  appointment = graphene.Field(AppointmentType)

  @classmethod
  def mutate(cls, root, info, id):

    if not info.context.user.is_superuser:
      return None

    appointment = Appointment.objects.get(pk=id)

    if not appointment:
      return None

    appointment.status = 'cancelled'
    appointment.cancelled_at = datetime.datetime.now()

    appointment.save()
    success = True

    return AppointmentCancellationMutation(
      appointment=appointment,
      success=success
    )
