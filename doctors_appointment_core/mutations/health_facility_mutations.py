import graphene
from graphene_django import DjangoObjectType

from doctors_appointment_core.graphql_types import HealthFacilityType
from doctors_appointment_core.models import HealthFacility

class HealthFacilityMutation(graphene.Mutation):
  class Arguments:
    # fields
    name = graphene.String(required=True)
    street_address_1 = graphene.String(required=True)
    street_address_2 = graphene.String()
    region = graphene.String(required=True)
    contact_number = graphene.String(required=True)
    email_address = graphene.String(required=False)
    id = graphene.ID()

  success = graphene.Boolean()
  health_facility = graphene.Field(HealthFacilityType)

  # TODO figure out how to implement a decorator to check user is admin / superuser
  @classmethod
  def mutate(cls, root, info, **kwargs):
    
    if not info.context.user.is_superuser:
      return None
    
    pk = kwargs.pop('id')

    if pk is not None:
      
      health_facility = HealthFacility.objects.get(pk=pk)
      
      for key, value in kwargs.items():
        setattr(health_facility, key, value)
    else:
      health_facility = HealthFacility(**kwargs)

    health_facility.save()

    success = True

    return HealthFacilityMutation(
      health_facility=health_facility,
      success=success
    )
