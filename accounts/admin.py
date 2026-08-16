from django.contrib import admin
from .models import Profile, Preference


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'age', 'gender', 'city', 'occupation')
    search_fields = ('full_name', 'city', 'user__username')


@admin.register(Preference)
class PreferenceAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'budget_min',
        'budget_max',
        'preferred_location',
        'food_preference',
        'smoking',
        'pets',
    )
    search_fields = ('user__username', 'preferred_location')