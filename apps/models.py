from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models import Model


class User(AbstractUser):
    phone = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    job = models.CharField(max_length=255)
    about_me = models.TextField()


class Skill(Model):
    user_id = models.ForeignKey('apps.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    level = models.IntegerField()


class Service(Model):
    user_id = models.ForeignKey('apps.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    dis = models.TextField()


class Portfolio(Model):
    user_id = models.ForeignKey('apps.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    title = models.TextField()
    type_choose = (
        ('Web Design', 'Web Design'),
        ('Gaming', 'Gaming'),
        ('Programming', 'Programming'),
        ('Graphic Design', 'Graphic Design')
    )
    category = models.CharField(max_length=255, choices=type_choose)
    dis = models.TextField()
    company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)


class Blog(Model):
    user_id = models.ForeignKey('apps.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_pics/', blank=True, null=True)
    title = models.CharField(max_length=255)
    dis = models.TextField()


class Comment(Model):
    name = models.CharField(max_length=255)
    author_id = models.ForeignKey('apps.User', on_delete=models.CASCADE)
    post_id = models.ForeignKey('apps.Blog', on_delete=models.CASCADE)
    text = models.TextField()
    email = models.EmailField(max_length=255, null=True, blank=True)
    date = models.DateField(auto_now_add=True)


