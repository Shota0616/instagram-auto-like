from django.urls import path
from user import views

urlpatterns = [
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile_edit'),
]