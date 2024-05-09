from rest_framework import serializers

from apps.transfer.models import HistoryTransfer

class HistoryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        fields = ('from_user', 'to_user', 'amount', 'is_completed', 'created_at')
        extra_kwargs = {
            'is_completed' : {'read_only': True},
            'created_at' : {'read_only': True},
            
        }
        