## Styling the Login Page

The login form is currently not well styled. Let's fix that.

---

### Implementing Bootstrap on the Login Form

In `login.html`...

```html
{% extends "learning_logs/base.html" %}
{% load django_bootstrap5 %}

{% block page_header %}
    <h2>Log in to your account.</h2>
{% endblock page_header %}

{% block content %}
    {% if form.errors %}
        <p>Your username and password didn't match. Please try again.</p>
    {% endif %}

    <form method="post" action="{% url 'accounts:login' %}">
        {% csrf_token %}
        {% bootstrap_form form %}
        {% bootstrap_button button_type="submit" content="Log in" %}
    </form>
{% endblock content %}
```

---

### Viewing the Styled Login Form

Now, if we visit the login page, we should see the styled form.

<img src="../../images/login_form_style.png" alt="Styled Login Form" style="width:500px;" />

---
