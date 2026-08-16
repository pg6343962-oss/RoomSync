from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

from django.contrib.auth.models import User
from .models import RoommateRequest


@login_required
def send_request(request, user_id):

    receiver = get_object_or_404(User, id=user_id)

    # User khud ko request nahi bhej sakta
    if receiver == request.user:
        messages.error(request, "You cannot send a request to yourself.")
        return redirect('find_roommates')

    # Check duplicate pending request
    existing_request = RoommateRequest.objects.filter(
        sender=request.user,
        receiver=receiver,
        status='pending'
    ).first()

    if existing_request:
        messages.info(request, "Roommate request already sent.")
        return redirect('view_profile', user_id=user_id)

    # Create new request
    RoommateRequest.objects.create(
        sender=request.user,
        receiver=receiver,
        status='pending'
    )

    messages.success(request, "Roommate request sent successfully!")

    return redirect('view_profile', user_id=user_id)

@login_required
def received_requests(request):

    requests = RoommateRequest.objects.filter(
        receiver=request.user
    ).select_related(
        'sender'
    ).order_by('-created_at')

    return render(
        request,
        'received_requests.html',
        {
            'requests': requests
        }
    )
    
@login_required
def update_request(request, request_id, action):

    roommate_request = get_object_or_404(
        RoommateRequest,
        id=request_id,
        receiver=request.user
    )

    if action == 'accept':
        roommate_request.status = 'accepted'

    elif action == 'reject':
        roommate_request.status = 'rejected'

    roommate_request.save()

    return redirect('received_requests')

@login_required
def sent_requests(request):

    requests = RoommateRequest.objects.filter(
        sender=request.user
    ).select_related(
        'receiver'
    ).order_by('-created_at')

    return render(
        request,
        'sent_requests.html',
        {
            'requests': requests
        }
    )    
