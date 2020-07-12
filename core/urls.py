
from django.urls import path

from core import views

urlpatterns = [
    path('', views.jobs, name='home')
]