from django.contrib import admin

# Register your models here.
from apps.users.models import User, HistoryTransfer

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'age')
    list_filter = ('id',)

@admin.register(HistoryTransfer)
class HistoryTransferAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user')
    list_filter = ('id',)