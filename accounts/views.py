from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile, Preference
from requests_app.models import RoommateRequest
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.shortcuts import get_object_or_404

def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, 'Account created successfully.')
        login(request, user)

        return redirect('profile-setup')

    return render(request, 'register.html')


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('profile-setup')

        messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def logout_view(request):

    logout(request)

    return redirect('home')


def profile_setup(request):

    if not request.user.is_authenticated:
        return redirect('login')

    profile = Profile.objects.filter(
        user=request.user
    ).first()

    if request.method == 'POST':

        full_name = request.POST.get('full_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        occupation = request.POST.get('occupation')
        bio = request.POST.get('bio')

        if profile is None:
            profile = Profile(
                user=request.user
            )

        profile.full_name = full_name
        profile.age = age
        profile.gender = gender
        profile.city = city
        profile.occupation = occupation
        profile.bio = bio

        if request.FILES.get('profile_photo'):
            profile.profile_photo = request.FILES['profile_photo']

        profile.save()

        messages.success(
            request,
            'Profile saved successfully!'
        )

        return redirect('preference_setup')

    return render(
        request,
        'profile_setup.html',
        {'profile': profile}
    )


def preference_setup(request):

    if not request.user.is_authenticated:
        return redirect('login')

    preference = Preference.objects.filter(
        user=request.user
    ).first()

    if request.method == 'POST':

        if preference is None:
            preference = Preference(user=request.user)

        preference.budget_min = request.POST.get('budget_min')
        preference.budget_max = request.POST.get('budget_max')
        preference.preferred_location = request.POST.get(
            'preferred_location'
        )
        preference.food_preference = request.POST.get(
            'food_preference'
        )

        preference.smoking = (
            request.POST.get('smoking') == 'yes'
        )

        preference.pets = (
            request.POST.get('pets') == 'yes'
        )

        preference.sleep_schedule = request.POST.get(
            'sleep_schedule'
        )

        preference.cleanliness = request.POST.get(
            'cleanliness'
        )

        preference.noise_preference = request.POST.get(
            'noise_preference'
        )

        preference.guests_preference = request.POST.get(
            'guests_preference'
        )

        preference.save()

        messages.success(
            request,
            'Preferences saved successfully!'
        )

        return redirect('home')

    return render(
        request,
        'preference_setup.html',
        {'preference': preference}
    )
    
    
def find_roommates(request):

    if not request.user.is_authenticated:
        return redirect('login')

    current_preference = Preference.objects.filter(
        user=request.user
    ).first()

    profiles = Profile.objects.exclude(
        user=request.user
    ).select_related('user')

    location = request.GET.get('location', '').strip()
    food = request.GET.get('food', '').strip()
    min_budget = request.GET.get('min_budget', '').strip()
    max_budget = request.GET.get('max_budget', '').strip()

    roommates = []
    print("TOTAL PROFILES:", Profile.objects.count())
    print("TOTAL PREFERENCES:", Preference.objects.count())
 

    for profile in profiles:

        other_preference = Preference.objects.filter(
            user=profile.user
        ).first()

        if not other_preference:
            continue

        # Location filter
        if location:
            if location.lower() not in (
                other_preference.preferred_location or ''
            ).lower():
                continue

        # Food filter
        if food:
            if other_preference.food_preference != food:
                continue

        # Minimum budget filter
        if min_budget:
            if other_preference.budget_max < int(min_budget):
                continue

        # Maximum budget filter
        if max_budget:
            if other_preference.budget_min > int(max_budget):
                continue

        # Compatibility score
        score = 0

        if current_preference:

            # Budget
            if (
                current_preference.budget_min
                <= other_preference.budget_max
                and
                other_preference.budget_min
                <= current_preference.budget_max
            ):
                score += 20

            # Location
            if (
                current_preference.preferred_location.lower()
                ==
                other_preference.preferred_location.lower()
            ):
                score += 20

            # Food
            if (
                current_preference.food_preference
                ==
                other_preference.food_preference
            ):
                score += 15

            # Smoking
            if (
                current_preference.smoking
                ==
                other_preference.smoking
            ):
                score += 15

            # Pets
            if (
                current_preference.pets
                ==
                other_preference.pets
            ):
                score += 10

            # Sleep schedule
            if (
                current_preference.sleep_schedule
                ==
                other_preference.sleep_schedule
            ):
                score += 20

        roommates.append({
            'profile': profile,
            'preference': other_preference,
            'score': score
        })

    roommates.sort(
        key=lambda x: x['score'],
        reverse=True
    )

    return render(
        request,
        'find_roommates.html',
        {
            'roommates': roommates,
            'location': location,
            'food': food,
            'min_budget': min_budget,
            'max_budget': max_budget,
        }
    )   
    
def view_profile(request, user_id):

    if not request.user.is_authenticated:
        return redirect('login')

    profile = Profile.objects.select_related(
        'user'
    ).filter(
        user_id=user_id
    ).first()

    if profile is None:
        return redirect('find_roommates')

    preference = Preference.objects.filter(
        user=profile.user
    ).first()

    return render(
        request,
        'view_profile.html',
        {
            'profile': profile,
            'preference': preference,
        }
    )
    
@login_required
def dashboard(request):

    profile = Profile.objects.filter(
        user=request.user
    ).first()

    preference = Preference.objects.filter(
        user=request.user
    ).first()

    sent_count = RoommateRequest.objects.filter(
        sender=request.user
    ).count()

    received_count = RoommateRequest.objects.filter(
        receiver=request.user
    ).count()

    accepted_count = RoommateRequest.objects.filter(
        receiver=request.user,
        status='accepted'
    ).count()

    return render(
        request,
        'dashboard.html',
        {
            'profile': profile,
            'preference': preference,
            'sent_count': sent_count,
            'received_count': received_count,
            'accepted_count': accepted_count,
        }
    )    
    
    
@login_required
def edit_profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():

            form.save()

            return redirect(
                'view_profile',
                user_id=request.user.id
            )

    else:

        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        'edit_profile.html',
        {
            'form': form
        }
    )    