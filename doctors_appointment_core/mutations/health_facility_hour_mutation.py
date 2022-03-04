import graphene
from graphene_django import DjangoObjectType

from doctors_appointment_core.models import HealthFacility, HealthFacilityHour

class HealthFacilityHourType(DjangoObjectType):
  class Meta:
    model = HealthFacilityHour
    fields = "__all__"


class HealthFacilityHourMutation(graphene.Mutation):
  class Arguments:
    related_facility = graphene.String(required=True)
    day_from = graphene.String()
    time_from = graphene.String()
    day_to = graphene.String()
    time_to = graphene.String()
    id = graphene.ID()

  success = graphene.Boolean()
  health_facility_hour = graphene.Field(HealthFacilityHourType)

  @classmethod
  def mutate(cls, root, info, **kwargs):

    print(kwargs['related_facility'])

    if not info.context.user.is_superuser:
      return None

    pk = kwargs.pop('id')

    related_facility_id = kwargs['related_facility']

    if related_facility_id is None:
      return None

    related_fac_obj = HealthFacility.objects.get(pk=kwargs['related_facility'])

    # check if the related facility exists
    if related_fac_obj is None:
      return None

    kwargs.pop('related_facility')

    if pk is not None:
      health_facility_hour = HealthFacilityHour.objects.get(pk=pk)
      for key, value in kwargs.items():
        setattr(health_facility_hour, key, value)
    else:
      health_facility_hour = HealthFacilityHour(**kwargs)

    health_facility_hour.related_facility = related_fac_obj
    health_facility_hour.save()
    success = True

    return HealthFacilityHourMutation(
      health_facility_hour=health_facility_hour,
      success=success
    )
