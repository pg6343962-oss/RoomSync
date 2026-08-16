from django.contrib import admin
from .models import RoommateRequest


@admin.register(RoommateRequest)
class RoommateRequestAdmin(admin.ModelAdmin):

    list_display = (
        'sender',
        'receiver',
        'status',
        'created_at',
    )

    list_filter = ('status',)

    search_fields = (
        'sender__username',
        'receiver__username',
    )