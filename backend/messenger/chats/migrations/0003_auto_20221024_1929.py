# Generated by Django 3.2.4 on 2022-10-24 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0002_auto_20221023_1709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'ordering': ('name',), 'verbose_name': 'Чат', 'verbose_name_plural': 'Чаты'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-created_at',), 'verbose_name': 'Сообщение', 'verbose_name_plural': 'Соообщения'},
        ),
        migrations.AlterField(
            model_name='chat',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_chats', to=settings.AUTH_USER_MODEL, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='kind',
            field=models.CharField(choices=[('P', 'Private'), ('G', 'Group')], max_length=2, null=True, verbose_name='тип'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='name',
            field=models.CharField(max_length=256, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='участники'),
        ),
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chats.chat', verbose_name='чат'),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='время создания'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(blank=True, default='', null=True, verbose_name='сообщение'),
        ),
        migrations.AlterField(
            model_name='message',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sent_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_from_messages', to=settings.AUTH_USER_MODEL, verbose_name='отправитель'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sent_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_to_messages', to=settings.AUTH_USER_MODEL, verbose_name='получатель'),
        ),
    ]
