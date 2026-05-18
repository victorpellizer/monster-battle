from rest_framework import mixins, viewsets

from django.db import transaction

from monster.models import Monster
from monster.nested_serializers_extended import MonsterListRetrieveUpdateSerializer


# Create your views here.

class MonsterListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for creating monsters.
    """

    queryset = Monster.objects.all().order_by("name")
    serializer_class = MonsterListRetrieveUpdateSerializer
    pagination_class = None
    authentication_classes = []
    permission_classes = []

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super(MonsterListCreateView, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(MonsterListCreateView, self).list(request, *args, **kwargs)
