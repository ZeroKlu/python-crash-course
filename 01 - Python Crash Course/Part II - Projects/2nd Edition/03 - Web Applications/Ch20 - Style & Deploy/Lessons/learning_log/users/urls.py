"""Defines URL patterns for users app"""

"""Defines URL patterns for users"""

import django
from atexit import register
from django.urls import path, include
from . import views

app_name = "users"
urlpatterns = [
    # Include default auth URLs (we don't need to create views for these - only templates)
    path("", include("django.contrib.auth.urls")),
    # Registration page (create view and template but use default form)
    path("register/", views.register, name = "register")
]