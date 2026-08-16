from django.contrib import admin
from .models import RoommateListing


@admin.register(RoommateListing)
class RoommateListingAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'user',
        'city',
        'locality',
        'monthly_rent',
        'room_type',
        'available_from',
        'is_active',
    )

    list_filter = (
        'city',
        'room_type',
        'is_active',
    )

    search_fields = (
        'title',
        'city',
        'locality',
    )