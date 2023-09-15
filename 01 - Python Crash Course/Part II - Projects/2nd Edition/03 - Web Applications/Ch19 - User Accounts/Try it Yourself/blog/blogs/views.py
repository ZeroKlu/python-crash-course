from django.shortcuts import get_object_or_404, redirect, render
from blogs.forms import BlogForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    """The home page for Blog"""
    if request.user.is_authenticated:
        blogs = BlogPost.objects.all().order_by("date_added")
    else:
        blogs = []
    context = {"blogs": blogs}
    return render(request, "blogs/index.html", context)

@login_required
def new_blog(request):
    if request.method != "POST":
        form = BlogForm()
    else:
        form = BlogForm(data = request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.save()
            return redirect("blogs:index")
    context = {"form": form}
    return render(request, "blogs/new_blog.html", context)

@login_required
def edit_blog(request, blog_id):
    blog = BlogPost.objects.get(id = blog_id)
    if blog.owner != request.user:
        return render(request, "blogs/invalid.html")
    if request.method != "POST":
        print("Not POST")
        form = BlogForm(instance = blog)
    else:
        form = BlogForm(instance = blog, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")
    context = {"blog": blog, "form": form}
    return render(request, "blogs/edit_blog.html", context)
