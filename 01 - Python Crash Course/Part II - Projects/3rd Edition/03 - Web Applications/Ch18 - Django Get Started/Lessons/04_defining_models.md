## Defining a Model

In programming, a *model* refers to a data structure with a specific set of attributes. In Django, a model is a class that represents a database table. A model is defined by a class that inherits `django.db.models.Model`.

---

### Creating The `Topic` Model

A user will have to be able to add multiple topic to their learning 
log. We will define a model to represent each topic.

We'll add two attributes to our model: `text` and `date_added`.

In `models.py`...

```python
"""Django Application Models"""

from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return str(self.text)
```

---

### Activating the Model

Before we can use a model, Django needs to know where it is. We need to add the application to the `INSTALLED_APPS` list in `settings.py`.

In `settings.py`...

```python
-- SNIP --

INSTALLED_APPS = [
    # My Apps
    'learning_logs',

    # Default Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

---

### Updating the Database

Now, we need to update the database to include our new model. We can do this by running the following command:

```powershell
python manage.py makemigrations learning_logs
```

Expected Output:

```
Migrations for 'learning_logs':
  learning_logs\migrations\0001_initial.py
    + Create model Topic
```

---

### Applying the Changes

Then, we can finalize the changes by running the following command:

```powershell
python manage.py migrate
```

Expected Output:

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0001_initial... OK
```

---
