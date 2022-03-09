import graphene

from doctors_appointment_core.graphql_types import SpecialistType
from doctors_appointment_core.models import Specialist, HealthFacility

class SpecialistMutation(graphene.Mutation):
  class Arguments:
    full_name = graphene.String(required=True)
    related_facility = graphene.String()
    date_started = graphene.String()
    id = graphene.ID()

  success = graphene.Boolean()
  specialist = graphene.Field(SpecialistType)

  @classmethod
  def mutate(cls, root, info, **kwargs):
    
    if not info.context.user.is_superuser:
      return None

    related_facility_id = kwargs['related_facility']

    related_facility_instance = HealthFacility.objects.get(pk=related_facility_id)

    if not related_facility_instance:
      return None

    kwargs.pop('related_facility')

    pk = kwargs.pop('id')

    if pk is not None:
      specialist = Specialist.objects.get(pk=pk)
      for key, value in kwargs.items():
        setattr(specialist, key, value)
    else:
      specialist = Specialist(**kwargs)

    specialist.related_facility = related_facility_instance
    specialist.save()
    success = True

    return SpecialistMutation(
      specialist=specialist,
      success=success
    )
