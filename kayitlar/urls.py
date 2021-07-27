from django.urls import path
from . import views

urlpatterns = [
    path('calisan/', views.calisan, name='calisan'),
]