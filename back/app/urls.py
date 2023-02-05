from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('app', views.AutoLikeView.as_view(), name='app'),
    path('confirm', views.AutoLikeConfirmView.as_view(), name='confirm'),
]