""" Defines URL patterns for learning_logs"""
from django.urls import path

from . import views

app_name = "learning_logs"
urlpatterns = [
    # Home Page
	path("", views.index, name = "index"),
    # Topics Page
    path("topics/", views.topics, name = "topics"),
    # Detail Page for Specific Topic
    path("topics/<int:topic_id>/", views.topic, name = "topic"),
]
