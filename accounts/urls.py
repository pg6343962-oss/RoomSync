from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile-setup/', views.profile_setup, name='profile-setup'),
    path('preferences/', views.preference_setup, name='preference_setup'),
    path('find-roommates/',views.find_roommates,name='find_roommates'),
    path('profile/<int:user_id>/', views.view_profile,name='view_profile'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path( 'edit-profile/', views.edit_profile, name='edit_profile'),
 ]