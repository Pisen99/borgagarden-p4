from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', index_view, name='index')
]
