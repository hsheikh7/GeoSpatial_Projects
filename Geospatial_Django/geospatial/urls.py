from django.urls import path
from geospatial.views import *
from django.contrib.auth import views as auth_views
# from . import views

urlpatterns = [
   path('',home, name='home')
   
]