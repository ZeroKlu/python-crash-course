## Styling the Topics Page

The topics page is currently not well styled. Let's fix that.

---

### Implementing Bootstrap on the Topics Page

In `topics.html`...

```html
{% extends 'learning_logs/base.html' %}

{% block page_header %}
    <h1>Topics</h1>
{% endblock page_header %}

{% block content %}
<ul class="list-group border-bottom pb-2 mb-4">
    {% for topic in topics %}
    <li class="list-group-item border-0">
        <a href="{% url 'learning_logs:topic' topic.id %}">
            {{ topic.text }}
        </a>
    </li>
    {% empty %}
    <li class="list-group-item border-0">No topics have been added yet.</li>
    {% endfor %}
</ul>

<a href="{% url 'learning_logs:new_topic' %}">Add a new topic</a>
{% endblock content %}
```

---

### Viewing the Topics Page

Now, if we visit the topics page, we should see the Bootstrap styling.

<img src="../../images/topics_style.png" alt="Topics Page with Bootstrap styling" style="width:500px;">

---
