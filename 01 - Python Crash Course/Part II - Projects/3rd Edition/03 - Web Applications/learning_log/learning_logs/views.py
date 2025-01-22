"""Views for learning_logs."""

from django.shortcuts import render
from .models import Topic

def index(request):
    """The home page for learning_logs."""
    return render(request, "learning_logs/index.html")

def topics(request):
    """Show all topics."""
    # pylint: disable=no-member
    topic_list = Topic.objects.order_by("date_added")
    context = {"topics": topic_list}
    return render(request, "learning_logs/topics.html", context)
