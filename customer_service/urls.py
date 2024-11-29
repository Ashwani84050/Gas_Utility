from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_request, name='create_request'),
    path('request/<int:pk>/', views.request_details, name='request_details'),
    path('', views.index, name='index'),
]
