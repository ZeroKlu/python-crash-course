"""Views for learning_logs."""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """The home page for learning_logs."""
    return render(request, "learning_logs/index.html")

@login_required
def topics(request):
    """Show all topics."""
    # pylint: disable=no-member
    topic_list = Topic.objects.filter(owner=request.user) \
        .order_by("date_added")
    context = {"topics": topic_list}
    return render(request, "learning_logs/topics.html", context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    # pylint: disable=no-member
    topic_item = Topic.objects.get(id=topic_id)
    if not check_topic_owner(topic_item, request.user):
        raise Http404
    entries = topic_item.entry_set.order_by("date_added")
    context = {"topic": topic_item, "entries": entries}
    return render(request, "learning_logs/topic.html", context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic_item = form.save(commit=False)
            new_topic_item.owner = request.user
            new_topic_item.save()
            return redirect("learning_logs:topics")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    # pylint: disable=no-member
    topic_item = Topic.objects.get(id=topic_id)
    if not check_topic_owner(topic_item, request.user):
        raise Http404

    if request.method != "POST":
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry_item = form.save(commit=False)
            new_entry_item.topic = topic_item
            new_entry_item.save()
            return redirect("learning_logs:topic", topic_id=topic_id)

    # Display a blank or invalid form.
    context = {"topic": topic_item, "form": form}
    return render(request, "learning_logs/new_entry.html", context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    # pylint: disable=no-member
    entry = Entry.objects.get(id=entry_id)
    topic_item = entry.topic
    if not check_topic_owner(topic_item, request.user):
        raise Http404
    if request.method != "POST":
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topic", topic_id=topic_item.id)

    # Display a blank or invalid form.
    context = {"entry": entry, "topic": topic_item, "form": form}
    return render(request, "learning_logs/edit_entry.html", context)

def check_topic_owner(topic_item, user):
    """Check that the user is the owner of the topic."""
    return topic_item.owner == user
