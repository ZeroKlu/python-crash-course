from django.shortcuts import get_object_or_404, redirect, render
from blogs.forms import BlogForm, DeleteBlogForm, CommentForm, DeleteCommentForm
from .models import BlogPost, BlogComment
from django.contrib.auth.decorators import login_required
import xlwt
from django.http import HttpResponse

def index(request):
    """The home page for Blog"""
    if request.user.is_authenticated:
        blogs = BlogPost.objects.all().order_by("-date_added")
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
            new_blog.owner = request.user
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
        form = BlogForm(instance = blog)
    else:
        form = BlogForm(instance = blog, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")
    context = {"blog": blog, "form": form}
    return render(request, "blogs/edit_blog.html", context)

@login_required
def delete_blog(request, blog_id):
    blog = BlogPost.objects.get(id = blog_id)
    if blog.owner != request.user:
        return render(request, "blogs/invalid.html")
    if request.method != "POST":
        form = DeleteBlogForm(instance = blog)
    else:
        form = DeleteBlogForm(instance = blog, data = request.POST)
        if form.is_valid():
            if request.POST["confirm"] == "yes": blog.delete()
            return redirect("blogs:index")
    context = {"blog": blog, "form": form}
    return render(request, "blogs/delete_blog.html", context)

@login_required
def add_comment(request, blog_id):
    blog = BlogPost.objects.get(id = blog_id)
    if request.method != "POST":
        form = CommentForm()
    else:
        form = CommentForm(data = request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.blog = blog
            comment.owner = request.user
            comment.save()
            return redirect("blogs:blog_details", blog_id = blog_id)
    context = {"blog": blog, "form": form}
    return render(request, "blogs/add_comment.html", context)

@login_required
def edit_comment(request, comment_id):
    comment = BlogComment.objects.get(id = comment_id)
    blog = comment.blog
    if comment.owner != request.user:
        return render(request, "blogs/invalid.html")
    if request.method != "POST":
        form = CommentForm(instance = comment)
    else:
        form = CommentForm(instance = comment, data = request.POST)
        if form.is_valid:
            form.save()
            return redirect("blogs:blog_details", blog_id = blog.id)
    context = {"comment": comment, "form": form}
    return render(request, "blogs/edit_comment.html", context)

@login_required
def delete_comment(request, comment_id):
    comment = BlogComment.objects.get(id = comment_id)
    blog = comment.blog
    if comment.owner != request.user:
        return render(request, "blogs/invalid.html")
    if request.method != "POST":
        form = DeleteCommentForm(instance = comment)
    else:
        form = DeleteCommentForm(instance = comment, data = request.POST)
        if form.is_valid():
            if request.POST["confirm"] == "yes": comment.delete()
            return redirect("blogs:blog_details", blog_id = blog.id)
    context = {"comment": comment, "form": form}
    return render(request, "blogs/delete_comment.html", context)

@login_required
def blog_details(request, blog_id):
    blog = BlogPost.objects.get(id = blog_id)
    comments = BlogComment.objects.filter(blog = blog)
    context = {"blog": blog, "comments": comments}
    return render(request, "blogs/blog_details.html", context)
    
@login_required
def export_blogs(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="blogs.xls"'
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet("BlogPosts & Comments")
    columns = ["Type", "ID", "Owner", "Title", "Text", "Date"]
    row_num = 0
    for col_num in range(len(columns)):
        worksheet.write(row_num, col_num, columns[col_num])
    blogs = BlogPost.objects.all()
    for blog in blogs:
        row_num += 1
        date_info = blog.date_added.strftime("%m/%d/%Y, %H:%M:%S")
        blog_data = ["BlogPost", blog.id, blog.owner.username, blog.title, blog.text, date_info]
        for col_num in range(len(blog_data)):
            worksheet.write(row_num, col_num, blog_data[col_num])
        comments = BlogComment.objects.filter(blog = blog)
        for comment in comments:
            row_num += 1
            date_info = comment.date_added.strftime("%m/%d/%Y, %H:%M:%S")
            comment_data = ["Comment", comment.id, comment.owner.username, comment.blog.title, comment.text, date_info]
            for col_num in range(len(comment_data)):
                worksheet.write(row_num, col_num, comment_data[col_num])
    workbook.save(response)
    return response
