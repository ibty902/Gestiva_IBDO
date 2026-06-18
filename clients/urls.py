from django.urls import path
from . import views

urlpatterns = [
     path('', views.dashboard, name='dashboard'),
    path('', views.clients, name='home'),
    path('clients/', views.clients, name='clients'),

]