# Generated by Django 3.2.4 on 2022-11-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_remove_message_sent_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='прочитано'),
        ),
    ]
