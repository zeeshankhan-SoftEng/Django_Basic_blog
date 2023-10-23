
from django.db import models
import uuid
from home.utils.validators import validate_content_length

class Blog_Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=600, unique=True, )
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[validate_content_length])

class Author(models.Model):
    name = models.CharField(max_length=100, default="unknown")

class Comment(models.Model):
    blog_post = models.ForeignKey(Blog_Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateField(auto_now_add=True)