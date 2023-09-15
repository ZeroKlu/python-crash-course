from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """A post from the user"""
    
    title = models.CharField(max_length = 50)
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    
    class Meta:
        verbose_name_plural = "blogs"

    def __str__(self):
        """Return a string representation of the model"""
        return self.title

