""" Defines URL patterns for blogs"""
from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.index, name="index"),
    path("new_blog/", views.new_blog, name="new_blog"),
    path("edit_blog/<int:blog_id>/", views.edit_blog, name="edit_blog"),
    path("delete_blog/<int:blog_id>/", views.delete_blog, name="delete_blog"),
    path("blog_details/<int:blog_id>/", views.blog_details, name="blog_details"),
    path("add_comment/<int:blog_id>/", views.add_comment, name="add_comment"),
    path("edit_comment/<int:comment_id>/", views.edit_comment, name="edit_comment"),
    path("delete_comment/<int:comment_id>/", views.delete_comment, name="delete_comment"),
    path("export_blogs/", views.export_blogs, name="export_blogs"),
]