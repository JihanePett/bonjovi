from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('bjcards/', views.bjcards, name='bjcards'),
    path('music/', views.music, name='music'),
    path('tours/', views.tours, name='tours'),
]
