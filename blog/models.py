from django.contrib.auth.models import AbstractUser
from django.db import models


STATUS=[
    ("active","active"),
    ("deleted","deleted")
]
# Create your models here.
class User(AbstractUser):
    pass

class Category(models.Model):
    name=models.CharField(max_length=30)
    def serialize(self):
        return {
            "name":self.name,
        }

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name="author")
    title=models.CharField(max_length=200)
    content=models.TextField()
    image = models.ImageField(upload_to='blog1/')
    likes=models.ManyToManyField(User,related_name="likes",blank=True)
    field=models.ForeignKey(Category,on_delete=models.CASCADE, related_name="category_field")
    status=models.CharField(max_length=7, choices=STATUS, default="active")
    date=models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "author":self.author,
            "title":self.title,
            "content":self.content,
            "image":self.image,
            "likes":self.likes.all().count(),
            "field":self.field,
            "status":self.status,
            "date":self.date.strftime("%b %d %Y, %I:%M %p"),
        }

class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")
    c_post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comment_post")
    body=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "user":self.user,
            "c_post":self.c_post,
            "body":self.body,
            "time":self.time
        }

class Contact(models.Model):
    sender=models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    subject=models.CharField(max_length=30)
    text=models.TextField()

    def serialize(self):
        return {
            "sender":self.sender,
            "subject":self.subject,
            "text":self.text
        }