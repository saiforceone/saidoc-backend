import graphene
from graphene_django import DjangoObjectType

from .models import CancellationReason

class CancellationReasonType(DjangoObjectType):
  class Meta:
    model = CancellationReason
    fields = ("id", "title", "description")


class Query(graphene.ObjectType):
  all_cancellation_reasons = graphene.List(CancellationReasonType)

  def resolve_all_cancellation_reasons(root, info):
    return CancellationReason.objects.all()

schema = graphene.Schema(query=Query)
