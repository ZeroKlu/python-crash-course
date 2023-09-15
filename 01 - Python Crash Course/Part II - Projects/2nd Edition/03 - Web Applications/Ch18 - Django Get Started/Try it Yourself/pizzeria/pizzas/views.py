from django.shortcuts import get_object_or_404, render
from .models import Pizza, Topping

def index(request):
    return render(request, "pizzas/index.html")

def pizzas(request):
    pizzas = Pizza.objects.all()
    context = {"pizzas": pizzas}
    return render(request, "pizzas/pizzas.html", context)

def pizza(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    toppings = Topping.objects.filter(pizza=pizza)
    context = {"pizza": pizza, "toppings": toppings}
    return render(request, "pizzas/pizza.html", context)
