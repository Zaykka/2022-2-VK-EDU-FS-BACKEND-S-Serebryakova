from chats.models import Chat, Message
from rest_framework import serializers


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ("id", "name", "kind", "photo", "author", "users")


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            "id",
            "message",
            "created_at",
            "photo",
            "chat",
            "sent_from",
            "is_read",
        )
