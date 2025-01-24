## Styling the Home Page

We'll modify the home page to make it more attractive.

### Adding a Jumbotron

Add a jumbotron to the home page, and add some text to the jumbotron.

In `learning_logs/templates/learning_logs/index.html`:

```html
{% extends 'learning_logs/base.html' %}

{% block page_header %}
    <div class="p-3 mb-4 bg-light border rounded-3">
        <div class="container-fluid py-4">
            {% if request.user.is_authenticated %}
                <h1 class="display-3">Welcome back, {{ request.user.username }}!</h1>
                <p class="lead">
                    Let's continue learning!
                </p>
            {% else %}
            <h1 class="display-3">Track your learning.</h1>
            <p class="lead">
                Make your own Learning Log, and keep a list of the 
                topics you're learning about. Whenever you learn something
                new about a topic, make an entry summarizing what you've
                learned.
            </p>
            <a class="btn btn-primary btn-lg mt-1" href="{% url 'accounts:register' %}">
                Register &raquo;
            </a>
            {% endif %}
        </div>
    </div>
{% endblock page_header %}
```

> Note: If you followed the book exactly, you'll notice that I added the
> `{% if request.user.is_authenticated %}` section. I didn't like defaulting
> to a "Register" button for an already registered (and logged-in) user.

---

### Viewing the Home Page

Refreshing the home page will show a "Register" button when not logged in...

<img src="../../images/index_style.png" alt="Styling the Home Page" style="width:500px;">

... or a "Welcome back" message when logged in.

<img src="../../images/index_style_logged_in.png" alt="Styling the Home Page" style="width:500px;">

---
