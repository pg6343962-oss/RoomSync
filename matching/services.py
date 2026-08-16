def calculate_compatibility(user1_preferences, user2_preferences):
    score = 0

    # 1. Budget - 20 points
    if (
        user1_preferences.budget_min <= user2_preferences.budget_max
        and
        user2_preferences.budget_min <= user1_preferences.budget_max
    ):
        score += 20

    # 2. Location - 20 points
    if (
        user1_preferences.preferred_location.strip().lower()
        == user2_preferences.preferred_location.strip().lower()
    ):
        score += 20

    # 3. Food preference - 15 points
    if (
        user1_preferences.food_preference
        == user2_preferences.food_preference
        or
        user1_preferences.food_preference == 'both'
        or
        user2_preferences.food_preference == 'both'
    ):
        score += 15

    # 4. Smoking - 10 points
    if user1_preferences.smoking == user2_preferences.smoking:
        score += 10

    # 5. Pets - 10 points
    if user1_preferences.pets == user2_preferences.pets:
        score += 10

    # 6. Sleep schedule - 10 points
    if (
        user1_preferences.sleep_schedule.lower()
        == user2_preferences.sleep_schedule.lower()
    ):
        score += 10

    # 7. Cleanliness - 5 points
    cleanliness_difference = abs(
        user1_preferences.cleanliness
        - user2_preferences.cleanliness
    )

    if cleanliness_difference <= 1:
        score += 5

    # 8. Noise preference - 5 points
    noise_difference = abs(
        user1_preferences.noise_preference
        - user2_preferences.noise_preference
    )

    if noise_difference <= 1:
        score += 5

    # 9. Guests preference - 5 points
    guests_difference = abs(
        user1_preferences.guests_preference
        - user2_preferences.guests_preference
    )

    if guests_difference <= 1:
        score += 5

    return score