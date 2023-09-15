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
    # User Add Topic Page
    path("new_topic/", views.new_topic, name = "new_topic"),
    # User Add Entry Page
    path("new_entry/<int:topic_id>/", views.new_entry, name = "new_entry"),
    # User Edit Entry Page
    path("edit_entry/<int:entry_id>/", views.edit_entry, name = "edit_entry"),
]
