from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from apps.models import User, Service, Blog, Skill, Comment, Portfolio
from django.forms import Form, CharField, EmailField

class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'image', 'phone', 'job', 'about_me', 'email', 'username', 'password']


class ServisModelForm(ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'dis', 'user_id']


class BlogModelForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['image', 'title', 'dis', 'user_id']


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'phone', 'job', 'about_me', 'email', 'password']


class AddSkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['title', 'level', 'user_id']


class PortfolioModelForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['user_id', 'image', 'dis', 'category', 'company', 'title']


class CommentsForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'email', 'name', 'post_id', 'author_id']


class ContactForm(Form):
    name = CharField(max_length=255)
    email = EmailField(max_length=255)
    message = CharField()