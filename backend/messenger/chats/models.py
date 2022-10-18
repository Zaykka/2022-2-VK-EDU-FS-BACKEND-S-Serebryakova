from django.db import models
from users.models import User


class Chat(models.Model):
    chat_name = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    chat_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

class Message(models.Model):
    chat_id = models.ManyToManyField(Chat)
    user_id = models.ManyToManyField(User)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')



