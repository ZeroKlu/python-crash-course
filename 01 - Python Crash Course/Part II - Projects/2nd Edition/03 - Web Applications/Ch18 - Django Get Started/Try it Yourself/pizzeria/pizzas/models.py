from unicodedata import name
from django.db import models

class Pizza(models.Model):
    """A named pizza"""
    name = models.CharField(max_length=30)
    def __str__(self):
        """String representation of the pizza model"""
        return self.name

class Topping(models.Model):
    """A pizza topping"""
    name = models.CharField(max_length=30)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    def __str__(self):
        """String representation of the topping model"""
        return self.name
