"""ModelForms for the learning_logs app."""

from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Form for the Topic model."""

    class Meta:
        """Metadata for the TopicForm."""
        model = Topic
        fields = ["text"]
        labels = {"text": ""}

class EntryForm(forms.ModelForm):
    """Form for the Entry model."""

    class Meta:
        """Metadata for the EntryForm."""
        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
