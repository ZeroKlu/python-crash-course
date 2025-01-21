## The Django Shell

From the terminal, we can interact with the tables in the database 
using the Django shell.

This shell is super-useful, since it allows us to test the code we 
will use when we start building the user interface pages.

---

### Using the Django Shell

To launch the Django shell, type the following command:

```powershell
python manage.py shell
```

Here's an example of a Django shell session:

```
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.   
(InteractiveConsole)
>>> from learning_logs.models import Topic
>>> topics = Topic.objects.all()
>>> for topic in topics:
...     print(topic.id, topic)
... 
1 Chess
2 Rock Climbing
```

---

### Querying for a Specific Topic

We can query individual items by ID like this:

```
>>> t = Topic.objects.get(id=1)
>>> t.text
'Chess'
>>> t.date_added
datetime.datetime(2025, 1, 20, 19, 56, 38, 521452, tzinfo=datetime.timezone.utc)
```

---

### Getting Related Entries

Now we can obtain the entries associated with that topic:

Notice how we use the name of the model (in lowercase) followed by
`_set` to define the query set `entry_set`.

```
>>> entries = t.entry_set.all()
>>> for entry in entries:
...     print("\n", entry.id, entry)
... 

1 Openings:

The opening is the first part of the

2 Bishops and Knights:

In the opening phase of th
```

---

### Closing the Django Shell

When we're done with the shell, we can close it by entering 

```powershell
>>> exit()
```

---
