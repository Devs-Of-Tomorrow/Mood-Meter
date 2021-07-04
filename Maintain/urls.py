from django.urls import path
from Maintain.views import Emphome
# from django.contrib import admin

urlpatterns = [
    path('', Emphome.as_view(), name='emphome'),

]
