## User Logout

Django provides a built-in logout feature that can be used to log a
user out of the site.

---

### The Logout Form

We can add a logout form to the base template to log a user out of the
site and limit it to only be displayed if the user is logged in.

In `base.html`...

```html
-- SNIP --

{% block content %}{% endblock content %}

<hr>
{% if user.is_authenticated %}
    <form action="{% url 'accounts:logout' %}" method="post">
        {% csrf_token %}
        <button name="submit">Log out</button>
    </form>
{% endif %}
```

---

### LOGOUT_REDIRECT_URL

Currently, if a user logs out, they will be redirected to the admin
page. We'll change that by updating the `settings.py` file...

```python
-- SNIP --

LOGOUT_REDIRECT_URL = "learning_logs:index"
```

---

### Testing Logout

While logged in, we will be presented with the logout button.

<img src="../../images/logout_form.png" alt="Logout button" style="width:320px;" />

Clicking the logout button will log the user out and redirect them to
the home page.

<img src="../../images/logged_out.png" alt="Logged out" style="width:320px;" />

---
