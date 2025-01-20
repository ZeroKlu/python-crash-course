"""Defines the admin site for learning_logs."""

from django.contrib import admin

from .models import Topic

admin.site.register(Topic)
