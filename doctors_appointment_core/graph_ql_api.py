import graphene
from graphene_django import DjangoObjectType

from .models import *
class CancellationReasonType(DjangoObjectType):
  class Meta:
    model = CancellationReason
    fields = ("id", "title", "description")


class EmergencyContactType(DjangoObjectType):

  class Meta:
    model = EmergencyContact
    fields = "__all__"

class HealthFacilityType(DjangoObjectType):

  class Meta:
    model = HealthFacility
    fields = "__all__"


class SpecialistType(DjangoObjectType):

  class Meta:
    model = Specialist
    fields = "__all__"


class SpecializationType(DjangoObjectType):

  class Meta:
    model = Specialization
    fields = "__all__"

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

schema = graphene.Schema(query=Query)
