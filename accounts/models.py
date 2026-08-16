from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    OCCUPATION_CHOICES = [
        ('student', 'Student'),
        ('working', 'Working'),
        ('other', 'Other'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )
    city = models.CharField(max_length=100)
    occupation = models.CharField(
        max_length=20,
        choices=OCCUPATION_CHOICES
    )
    bio = models.TextField(blank=True)

    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.full_name


class Preference(models.Model):

    FOOD_CHOICES = [
        ('veg', 'Vegetarian'),
        ('non_veg', 'Non-Vegetarian'),
        ('both', 'Both'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    budget_min = models.PositiveIntegerField()
    budget_max = models.PositiveIntegerField()
    preferred_location = models.CharField(max_length=100)

    food_preference = models.CharField(
        max_length=20,
        choices=FOOD_CHOICES
    )

    smoking = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)

    sleep_schedule = models.CharField(max_length=50)

    cleanliness = models.PositiveIntegerField(default=3)
    noise_preference = models.PositiveIntegerField(default=3)
    guests_preference = models.PositiveIntegerField(default=3)

    def __str__(self):
        return f"{self.user.username}'s Preferences"