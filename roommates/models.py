from django.db import models
from django.contrib.auth.models import User


class RoommateListing(models.Model):

    ROOM_TYPE_CHOICES = [
        ('private', 'Private Room'),
        ('shared', 'Shared Room'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='roommate_listings'
    )

    title = models.CharField(max_length=150)

    description = models.TextField()

    city = models.CharField(max_length=100)

    locality = models.CharField(max_length=100)

    monthly_rent = models.PositiveIntegerField()

    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPE_CHOICES
    )

    available_from = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title