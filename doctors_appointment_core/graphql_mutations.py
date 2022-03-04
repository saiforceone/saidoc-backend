import graphene
from graphene_django import DjangoObjectType

from doctors_appointment_core.mutations.cancellation_mutations import CreateCancellationReason
from .mutations.health_facility_mutations import HealthFacilityMutation
from .mutations.health_facility_hour_mutation import HealthFacilityHourMutation


class CoreMutations(graphene.ObjectType):
  create_cancellation_reason = CreateCancellationReason.Field()
  create_health_facility = HealthFacilityMutation.Field()
  create_health_facility_hour = HealthFacilityHourMutation.Field()
