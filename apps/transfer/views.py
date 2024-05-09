from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework import serializers

from apps.transfer.models import HistoryTransfer
from apps.transfer.serializers import HistoryTransferSerializer
from apps.users.models import User  
# Create your views here.
class HistoryTransferAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    queryset = HistoryTransfer.objects.all()
    serializer_class = HistoryTransferSerializer

    # def get_permissions(self):
    #     if self.action in ('update', 'partial_update', 'destroy'):
    #         return (UserPermissons(), )
    #     return (AllowAny(), )