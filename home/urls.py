from django.urls import path
from . import views

# how to get home view from home app

urlpatterns = [
    path('', views.home, name='home'),
]
