from distutils.command.upload import upload
from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    chat_id = models.ManyToManyField('chats.Chat')
