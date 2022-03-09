import graphene

from doctors_appointment_core.graphql_types import EmergencyContactType
from doctors_appointment_core.models import EmergencyContact


class EmergencyContactMutation(graphene.Mutation):
  class Arguments:
    id = graphene.ID()
    full_name = graphene.String(required=True)
    contact_number = graphene.String(required=True)
    email_address = graphene.String(required=True)
    relationship_to_user = graphene.String(required=True)

  success = graphene.Boolean()
  emergency_contact = graphene.Field(EmergencyContactType)

  @classmethod
  def mutate(cls, root, info, **kwargs):
    # TODO replace this with a decorator
    if not info.context.user.is_authenticated:
      return None

    pk = kwargs.pop('id')

    if pk is not None:
      emergency_contact = EmergencyContact.objects.get(pk=pk)
      for key, value in kwargs.items():
        setattr(emergency_contact, key, value)
    else:
      emergency_contact = EmergencyContact(**kwargs)

    emergency_contact.related_user = info.context.user
    emergency_contact.save()
    success = True

    return EmergencyContactMutation(
      emergency_contact=emergency_contact,
      success=success
    )
