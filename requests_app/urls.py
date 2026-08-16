from django.urls import path
from . import views

urlpatterns = [
    path('send-request/<int:user_id>/',views.send_request,name='send_request' ),
    path('received/',views.received_requests,name='received_requests'),
    path('update/<int:request_id>/<str:action>/',views.update_request,name='update_request'),
    path('sent/', views.sent_requests, name='sent_requests'),
]