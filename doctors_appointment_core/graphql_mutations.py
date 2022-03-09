import graphene
from graphene_django import DjangoObjectType

from doctors_appointment_core.mutations.cancellation_mutations import CreateCancellationReason
from .mutations.health_facility_mutations import HealthFacilityMutation
from .mutations.health_facility_hour_mutation import HealthFacilityHourMutation
from .mutations.specialist_mutations import SpecialistMutation
from .mutations.specialization_mutations import SpecializationMutation
from .mutations.appointment_mutations import AppointmentMutation, AppointmentUpdateMutation, AppointmentCancellationMutation
from .mutations.appointment_note_mutations import AppointmentNoteCreateMutation
from .mutations.emergency_contact_mutations import EmergencyContactMutation


class CoreMutations(graphene.ObjectType):
  create_cancellation_reason = CreateCancellationReason.Field()
  create_health_facility = HealthFacilityMutation.Field()
  create_health_facility_hour = HealthFacilityHourMutation.Field()
  create_specialist = SpecialistMutation.Field()
  create_specialization = SpecializationMutation.Field()
  create_appointment = AppointmentMutation.Field()
  update_appointment = AppointmentUpdateMutation.Field()
  cancel_appointment = AppointmentCancellationMutation.Field()
  create_appointment_note = AppointmentNoteCreateMutation.Field()
  create_emergency_contact = EmergencyContactMutation.Field()
  