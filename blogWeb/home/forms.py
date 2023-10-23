from django import forms
from home.models import Blog_Post, Comment,Author



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog_Post
        fields = ['title', 'content']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }
