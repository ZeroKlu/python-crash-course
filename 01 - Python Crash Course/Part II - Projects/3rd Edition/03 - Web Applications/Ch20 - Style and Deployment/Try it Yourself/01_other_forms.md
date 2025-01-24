## Assignment 20.1: Other Forms

We applied Bootstrap's styles to the login page. Make similar changes to the
rest of the form-based pages including new_topic, new_entry, edit_entry, and
register.

---

### new_topic.html

```html
{% extends "learning_logs/base.html" %}
{% load django_bootstrap5 %}

{% block page_header %}
    <h1>Add a new topic</h1>
{% endblock page_header %}

{% block content %}
    <form method="post" action="{% url 'learning_logs:new_topic' %}">
        {% csrf_token %}
        {% bootstrap_form form %}
        {% bootstrap_button button_type="submit" content="Add Topic" %}
    </form>
{% endblock content %}
```

<img src="../../images/add_topic_style.png" alt="Add Topic Form Styled" style="width:500px;">

---

### new_entry.html

```html
{% extends "learning_logs/base.html" %}
{% load django_bootstrap5 %}

{% block page_header %}
    <h1>
        <a href="{% url 'learning_logs:topic' topic.id %}">{{ topic.text }}</a>
        : Add a new entry
    </h1>
{% endblock page_header %}

{% block content %}
    <form action="{% url 'learning_logs:new_entry' topic.id %}" method="post">
        {% csrf_token %}
        {% bootstrap_form form %}
        {% bootstrap_button button_type="submit" content="Add entry" %}
    </form>
{% endblock content %}
```

<img src="../../images/add_entry_style.png" alt="Add Entry Form Styled" style="width:500px;">

---

### edit_entry.html

```html
{% extends "learning_logs/base.html" %}
{% load django_bootstrap5 %}

{% block page_header %}
    <h1>
        <a href="{% url 'learning_logs:topic' topic.id %}">{{ topic.text }}</a>
        : Edit entry
    </h1>
{% endblock page_header %}

{% block content %}
    <form action="{% url 'learning_logs:edit_entry' entry.id %}" method="post">
        {% csrf_token %}
        {% bootstrap_form form %}
        {% bootstrap_button button_type="submit" content="Save changes" %}
    </form>
{% endblock content %}
```

<img src="../../images/edit_entry_style.png" alt="Edit Entry Form Styled" style="width:500px;">

---

### register.html

```html
{% extends "learning_logs/base.html" %}
{% load django_bootstrap5 %}

{% block page_header %}
  <h1>Register</h1>
{% endblock page_header %}

{% block content %}
    <form action="{% url 'accounts:register' %}" method="post">
        {% csrf_token %}
        {% bootstrap_form form %}
        {% bootstrap_button button_type="submit" content="Register" %}
    </form>
{% endblock content %}
```

<img src="../../images/register_style.png" alt="Register Form Styled" style="width:500px;">

---
