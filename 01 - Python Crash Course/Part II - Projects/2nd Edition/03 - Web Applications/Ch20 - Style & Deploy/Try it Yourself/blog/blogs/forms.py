from dataclasses import fields
from pyexpat import model
from django import forms
from .models import BlogPost, BlogComment

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "text"]
        labels = {"title": "Title", "text": "Text"}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}

class DeleteBlogForm(forms.ModelForm):
    confirm = forms.ChoiceField(choices=[("yes", "yes"), ("no", "no")])
    class Meta:
        model = BlogPost
        fields = ["confirm"]
        labels = {"confirm": ""}

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ["text"]
        labels = {"text": "Text"}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}

class DeleteCommentForm(forms.ModelForm):
    confirm = forms.ChoiceField(choices=[("yes", "yes"), ("no", "no")])
    class Meta:
        model = BlogComment
        fields = ["confirm"]
        labels = {"confirm": ""}
        