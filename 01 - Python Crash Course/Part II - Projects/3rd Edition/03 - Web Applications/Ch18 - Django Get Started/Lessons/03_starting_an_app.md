## Starting an App

A Django project is composed of multiple *apps*, that work together to
provide the functionality of the project as a whole.

From this point on, it will be useful to have two terminals open. One
should contain the running server, and the other should be used to
manage the project.

---

### Starting the App

In the project management terminal, run the following command:

```powershell
python manage.py startapp learning_logs
```

This will create the `learning_logs` app in the `learning_log` directory, containing the following files.

```
─ learning_log
  ├─ learning_logs
     ├─ __init__.py
     ├─ admin.py
     ├─ apps.py
     ├─ models.py
     ├─ tests.py
     ├─ views.py
     └─ migrations
        └─ __init__.py
  └─ ...
```

---
