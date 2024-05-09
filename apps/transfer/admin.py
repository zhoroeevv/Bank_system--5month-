from django.contrib import admin

from apps.transfer.models import HistoryTransfer
# Register your models here.
@admin.register(HistoryTransfer)
class HistoryTransferAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'amount')
    list_filter = ('id',)