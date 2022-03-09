import graphene

from .models import *
from doctors_appointment_core.graphql_mutations import CoreMutations
from .graphql_types import *

class Query(graphene.ObjectType):
  all_cancellation_reasons = graphene.List(CancellationReasonType)

  def resolve_all_cancellation_reasons(root, info):
    return CancellationReason.objects.all()

  # -- emergency contacts
  emergency_contacts_for_user = graphene.List(EmergencyContactType)

  def resolve_emergency_contacts_for_user(root, info):
    if not info.context.user.is_authenticated:
      return None
    else:
      return EmergencyContact.objects.filter(related_user=info.context.user.id)

  # -- specialists
  all_specialists = graphene.List(SpecialistType)

  def resolve_all_specialists(root, info):
    return Specialist.objects.all()

  specialists_by_specialization = graphene.List(SpecializationType, specialization=graphene.String(required=True))

  def resolve_specialists_by_specialization(root, info, specialization):
    try:
      return Specialization.objects.filter(name=specialization)
    except Exception:
      return None

  # -- specializations 
  all_specializations = graphene.List(SpecializationType)

  def resolve_all_specializations(root, info):
    return Specialization.objects.all()

  # -- health facilities
  all_health_facilities = graphene.List(HealthFacilityType)

  def resolve_all_facilities(root, info):
    return HealthFacility.objects.all()

  facilities_by_region = graphene.List(HealthFacilityType, region=graphene.String(required=True))

  def resolve_facilities_by_region(root, info, region):
    try:
      return HealthFacility.objects.filter(region=region)
    except Exception:
      return None

  # -- health facility hours
  hours_by_facility = graphene.List(
    HealthFacilityHourType,
    facility=graphene.String(required=True)
  )

  def resolve_hours_by_facility(root, info, facility):
    if not facility:
      return None

    try:
      return HealthFacilityHour.objects.filter(related_facility=facility)
    except:
      return None

  # -- appointments
  # TODO make use of Django-filter to allow for more granular filtering of appointments
  appointments_for_user = graphene.List(AppointmentType)

  def resolve_appointments_for_user(root, info):
    if not info.context.user.is_authenticated:
      return None
    else:
      return Appointment.objects.filter(patient=info.context.user.id)

  # -- appointment notes
  appointment_notes_for_appt = graphene.List(
    AppointmentNoteType,
    appointment=graphene.String(required=True)
  )

  def resolve_appointment_notes_for_appt(root, info, appointment):
    if not info.context.user.is_authenticated:
      return None
    elif not appointment:
      return None
    else:
      try:
        appt = Appointment.objects.get(id=appointment, patient=info.context.user.id)
        return AppointmentNote.objects.filter(related_appointment=appt.id)
      except Exception:
        return None

  # user profiles --
  current_user_profile = graphene.Field(UserProfileType)

  def resolve_current_user_profile(root, info):
    if not info.context.user.is_authenticated:
      return None
    
    try:
      return UserProfile.objects.get(user=info.context.user)
    except:
      return None

  all_user_profiles = graphene.List(UserProfileType)

  def resolve_all_user_profiles(root, info):
    if not info.context.user.is_authenticated:
      return None

    print(info.context.user.__dict__)

    if not info.context.user.is_superuser:
      return None

    try:
      return UserProfile.objects.all().exclude(user=info.context.user)
    except:
      return None

schema = graphene.Schema(
  query=Query,
  mutation=CoreMutations
)
