# Generated by Django 3.2.4 on 2022-10-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chat_id',
            field=models.ManyToManyField(to='chats.Chat'),
        ),
    ]
