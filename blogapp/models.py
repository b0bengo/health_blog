from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """
    This model represents a blog post. It includes fields for the title, content, author, and date posted.
    The author field is a ForeignKey that links to the User model.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title