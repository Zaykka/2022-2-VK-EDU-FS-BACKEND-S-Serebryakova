from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=100, verbose_name='номер телефона')
    bio = models.TextField(null=True, verbose_name='описание профиля')
    is_online = models.BooleanField(default=False, verbose_name='онлайн')
    profile_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, verbose_name='фото профиля')

    def __str__(self):
            return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'