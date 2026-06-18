from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='clients'),
    path('', views.article_list, name='articles'),
]