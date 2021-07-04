from django.urls import path
from Maintain.views import Emphome, Signup

# from django.contrib import admin

urlpatterns = [
    path('', Emphome.as_view(), name='emphome'),
    path('signup', Signup.as_view(), name='signup'),

]
