import graphene
from graphene_django import DjangoObjectType

from doctors_appointment_core.models import CancellationReason

class CancellationReasonType(DjangoObjectType):
  class Meta:
    model = CancellationReason
    fields = ("title", "description")


class CreateCancellationReason(graphene.Mutation):
  class Arguments:
    title = graphene.String()
    description = graphene.String()

  success = graphene.Boolean()
  cancellation_reason = graphene.Field(CancellationReasonType)

  @classmethod
  def mutate(cls, root, info, title, description):
    if not info.context.user.is_authenticated:
      return None

    if not info.context.user.is_superuser:
      return None

    cancellation_reason = CancellationReason(
      title=title,
      description=description
    )
    cancellation_reason.save()

    success = True
    
    return CreateCancellationReason(
      cancellation_reason=cancellation_reason,
      success=success
    )