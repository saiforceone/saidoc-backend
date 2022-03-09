import graphene

from doctors_appointment_core.graphql_types import AppointmentNoteType
from doctors_appointment_core.models import Appointment, AppointmentNote

class AppointmentNoteCreateMutation(graphene.Mutation):
  class Arguments:
    id = graphene.ID()
    related_appointment = graphene.String(required=True)
    note = graphene.String(required=True)
  
  success = graphene.Boolean()
  appointment_note = graphene.Field(AppointmentNoteType)

  @classmethod
  def mutate(cls, root, info, id, related_appointment, note):
    
    if not info.context.user.is_superuser:
      return None

    appointment_instance = Appointment.objects.get(pk=related_appointment)

    if not appointment_instance:
      return None

    appointment_note = AppointmentNote(
      related_appointment=appointment_instance,
      note=note,
    )
    appointment_note.save()
    success = True
    
    return AppointmentNoteCreateMutation(
      appointment_note=appointment_note,
      success=success
    )
