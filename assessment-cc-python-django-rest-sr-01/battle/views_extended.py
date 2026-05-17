from django.db import transaction
from django.http import Http404
from rest_framework import mixins, viewsets
from battle.models_extended import Battle
from battle.serializers_extended import BattleListSerializer, BattleCreateSerializer
from monster.models import Monster
from battle.utils_extended import fight


# Create your views here.
class BattleListCreateView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for listing battles.
    """

    queryset = Battle.objects.all()
    serializer_class = BattleListSerializer
    serializer_create_class = BattleCreateSerializer
    pagination_class = None
    authentication_classes = []
    permission_classes = []

    def get_serializer_class(self):
        if self.action == "create":
            return self.serializer_create_class
        return self.serializer_class
    
    def create():
        #TODO
     raise NotImplementedError("The create function is not implemented yet.")


class BattleRetrieveDeleteView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for update, retrieve and delete battles.
    """

    queryset = Battle.objects.all()
    serializer_class = BattleListSerializer
    authentication_classes = []
    permission_classes = []

    @transaction.atomic
    def retrieve(self, request, *args, **kwargs):
        try:
            return super(BattleRetrieveDeleteView, self).retrieve(
                request, *args, **kwargs
            )
        except Http404:
            raise Battle.DoesNotExist

    def destroy():
        #TODO
     raise NotImplementedError("The create function is not implemented yet.")
