## Individual Topic Pages with Entries

In order to make the Learning Log useful, we want to be able to view 
an individual topic and its entries.

---

### The Topic URL

Creating a URL pattern for an individual topic requires including a
query in the URL to obtain the specified topic by ID.

In `learning_logs/urls.py`:

```python
-- SNIP --

urlpatterns = [
    -- SNIP --

    # Detail page for a single topic
    path("topics/<int:topic_id>/", views.topic, name="topic"),
]
```

---

### The Topic View

As before, we need to create the view for the topic page.

In `learning_logs/views.py`:

```python
-- SNIP --

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic_item = Topic.objects.get(id=topic_id)
    entries = topic_item.entry_set.order_by("date_added")
    context = {"topic": topic_item, "entries": entries}
    return render(request, "learning_logs/topic.html", context)
```

---

### The Topic Template

Now we need to create the template for the topic page.

In `learning_logs/templates/learning_logs/topic.html`...

```html
{% extends 'learning_logs/base.html' %}

{% block content %}
<p>Topic: {{ topic.text }}</p>
<p>Entries:</p>
<ul>
    {% for entry in entries %}
    <li>
        <p>{{ entry.date_added|date:'M d, Y H:i' }}</p>
        <p>{{ entry.text|linebreaks }}</p>
    </li>
    {% empty %}
    <li>There are no entries for this topic yet.</li>
    {% endfor %}
</ul>
{% endblock content %}
```

---

### Linking to the Topic Page

We now need to modify the entries in the `topics.html` page to link to
the individual topic pages.

In `learning_logs/templates/learning_logs/topics.html`:

```html
-- SNIP --

    {% for topic in topics %}
    <li>
        <a href="{% url 'learning_logs:topic' topic.id %}">
            {{ topic.text }}
        </a>
    </li>
    {% empty %}
    <li>No topics have been added yet.</li>
    {% endfor %}

-- SNIP --
```

---

### Validating the Topic Pages


