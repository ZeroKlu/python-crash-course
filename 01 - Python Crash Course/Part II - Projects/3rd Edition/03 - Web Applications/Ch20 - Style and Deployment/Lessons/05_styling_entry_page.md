## Styling Entries on the Topic Page

The entries page is currently not well styled. Let's fix that.

---

### Implementing Bootstrap on the Entries Page

In `topic.html`...

```html
{% extends 'learning_logs/base.html' %}

{% block page_header %}
    <h1>Topic: {{ topic.text }}</h1>
{% endblock page_header %}

{% block content %}
<p>
    <a href="{% url 'learning_logs:new_entry' topic.id %}">
        Add new entry
    </a>
</p>
{% for entry in entries %}
    <div class="card mb-3">
        <!-- Card header with timestamp and edit link -->
        <h4 class="card-header">
            {{ entry.date_added|date:'M d, Y H:i' }}
            <small>
                <a href="{% url 'learning_logs:edit_entry' entry.id %}">
                    edit entry
                </a>
            </small>
        </h4>
        <!-- Card body with entry text -->
        <div class="card-body">
            {{ entry.text|linebreaks }}
        </div>
    </div>
{% empty %}
    <li>There are no entries for this topic yet.</li>
{% endfor %}
{% endblock content %}
```

---

### Viewing the Entries Page

Now, when we view a specific topic, the entries appear as Bootstrap cards.

<img src="../../images/entries_style.png" alt="Entries page with Bootstrap cards" style="width:500px;">>

---

### Styling the Remaining Forms Pages

There are still several forms that need styling. They are covered in the 
Try-it-Yourself section.

[Styling Other Forms](../Try%20it%20Yourself/01_other_forms.md)

---
