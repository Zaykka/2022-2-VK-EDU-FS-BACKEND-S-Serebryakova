from django.conf.global_settings import AUTH_USER_MODEL
from django.conf import settings
from django.db import models


class Chat(models.Model):
    PRIVATE = 'P'
    GROUP = 'G'
    CHAT_TYPE_CHOICES = [
        (PRIVATE, 'Private'),
        (GROUP, 'Group')
    ]
    name = models.CharField(max_length=256, verbose_name='название') 
    kind = models.CharField(max_length=2, choices=CHAT_TYPE_CHOICES, null=True, verbose_name='тип') 
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, verbose_name='фото')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_chats', on_delete=models.SET_NULL, null=True, verbose_name='автор')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='участники')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ""

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        ordering = ('name',)



class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True, verbose_name='чат')
    sent_from = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_from_messages', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='отправитель')
    #sent_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_to_messages', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='получатель')
    message = models.TextField(blank=True, null=True, default='', verbose_name='сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, verbose_name='фото')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Соообщения'
        ordering = ('-created_at',)






