import graphene
from graphene_django import DjangoObjectType

from doctors_appointment_core.graphql_types import SpecializationType
from doctors_appointment_core.models import Specialist, Specialization

class SpecializationMutation(graphene.Mutation):
  class Arguments:
    id = graphene.ID()
    related_specialist = graphene.String(required=True)
    name = graphene.String(required=True)
    description = graphene.String()

  success = graphene.Boolean()
  specialization = graphene.Field(SpecializationType)

  @classmethod
  def mutate(cls, root, info, **kwargs):

    if not info.context.user.is_superuser:
      return None

    specialist_id = kwargs.pop('related_specialist')

    specialist_instance = Specialist.objects.get(pk=specialist_id)

    if not specialist_instance:
      return None

    pk = kwargs.pop('id')

    if pk is not None:
      specialization = Specialization.objects.get(pk=pk)
    else:
      specialization = Specialization(**kwargs)
    
    specialization.related_specialist = specialist_instance
    specialization.save()

    success = True

    return SpecializationMutation(
      specialization=specialization,
      success=success
    )
