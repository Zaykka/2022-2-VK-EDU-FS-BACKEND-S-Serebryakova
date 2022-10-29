from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=256, verbose_name='ник')
    first_name = models.CharField(max_length=256, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=256, null=True, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=100, verbose_name='номер телефона')
    bio = models.TextField(null=True, verbose_name='описание профиля')
    is_online = models.BooleanField(default=False, verbose_name='онлайн')
    profile_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, verbose_name='фото профиля')

    def __str__(self):
            return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'