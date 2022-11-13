from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from chats.models import Chat, Message
from users.models import User
from chats.serializers import ChatSerializer, MessageSerializer
from rest_framework import generics


# @require_http_methods(["GET", ])
# def chat_list(request, user_id):
#     """Получить список всех чатов"""

#     chats = []
#     user = get_object_or_404(User, id=user_id)
#     chats = ChatSerializer(Chat.objects.filter(users=user), many=True).data
#     return JsonResponse({'chats': chats}, status=200)


# @require_http_methods(["GET", ])
# def chat_detail(request, chat_id):
#     """Получить список сообщений по id чата"""

#     messages = []
#     chat = get_object_or_404(Chat, id=chat_id)
#     for message_meta in Message.objects.filter(chat=chat):
#         messages.append(
#             {'id': message_meta.id,
#              'sent_from': str(message_meta.sent_from),
#              'message': message_meta.message,
#              'created_at': message_meta.created_at,
#              'photo': str(message_meta.photo)})
#     return JsonResponse({'chats': messages}, status=200)


# @require_http_methods(["POST", ])
# def create_chat(request, id):
#     """Cоздать чат (минимальный набор полей: название, описание)"""

#     name = request.POST.get("name")
#     kind = request.POST.get('kind')
#     photo = request.POST.get('photo')
#     author = int(request.POST.get('author'))
#     users = request.POST.get('users')
#     author_object = get_object_or_404(User, id=author)
#     # TODO: проверка что чата с таким id нет
#     new_chat = Chat.objects.create(
#         id=id, name=name, kind=kind, photo=photo, author=author_object)

#     if users is not None:
#         users_queryset = User.objects.filter(id__in=users.split())
#         for user in users_queryset:
#             new_chat.users.add(user)
#     return JsonResponse({'created': True}, status=201)


# @require_http_methods(["PATCH", ])
# def edit_chat(request, id):
#     """Отредактировать чат по id (минимальный набор полей: название, описание)"""

#     chat = get_object_or_404(Chat, id=id)
#     name = request.POST.get("name")
#     kind = request.POST.get('kind')
#     photo = request.POST.get('photo')
#     author = request.POST.get('author')
#     users = request.POST.get('users')

#     if name is not None:
#         chat.name = name
#     if kind is not None:
#         chat.name = kind
#     if photo is not None:
#         chat.name = photo
#     if author is not None:
#         author_model = get_object_or_404(User, id=int(author))
#         chat.author = author_model

#     chat.save()
#     if users is not None:
#         users_queryset = User.objects.filter(id__in=users.split())
#         for user in users_queryset:
#             chat.users.add(user)

#     return JsonResponse({'edited': True}, status=200)


# @require_http_methods(["DELETE", ])
# def delete_chat(request, id):
#     """Удалить чат по id"""
#     chat = get_object_or_404(Chat, id=id)
#     chat.delete()
#     return JsonResponse({'deleted': True}, status=200)


# @require_http_methods(["POST", ])
# def add_user_to_chat(request, chat_id, user_id):
#     """Добавить участника в чат по id человека и id чата"""

#     user = get_object_or_404(User, id=user_id)
#     chat = get_object_or_404(Chat, id=chat_id)
#     if user in chat.users.all():
#         return JsonResponse({'add_user_to_chat': False, 'info': f'user {user.username} already in chat'}, status=400)
#     chat.users.add(user)
#     return JsonResponse({'add_user_to_chat': True}, status=200)


@require_http_methods(
    [
        "POST",
    ]
)
def delete_user_from_chat(chat_id, user_id):
    """Удалить участника из чата по id человека и id чата"""

    user = get_object_or_404(User, id=user_id)
    chat = get_object_or_404(Chat, id=chat_id)
    chat.users.remove(user)
    return JsonResponse({"delete_user_from_chat": True}, status=200)


# @require_http_methods(['POST', ])
# def create_message(request, chat_id):
#     """Отправить сообщение по id чата"""

#     chat = get_object_or_404(Chat, id=chat_id)
#     sent_from_id = int(request.POST.get('sent_from'))
#     sent_from = get_object_or_404(User, id=sent_from_id)
#     message = request.POST.get('message')
#     photo = request.POST.get('photo')
#     Message.objects.create(chat=chat, sent_from=sent_from,
#                            message=message, photo=photo)
#     return JsonResponse({'create_message': True}, status=201)


# @require_http_methods(['POST', ])
# def edit_message(request, message_id):
#     """Отредактировать сообщение по id сообщения"""

#     message = get_object_or_404(Message, id=message_id)
#     new_message = request.POST.get('message')
#     print('new_message: ', new_message)
#     message.message = new_message
#     message.save()
#     return JsonResponse({'Message edited': True}, status=200)


# @require_http_methods(['POST', ])
# def make_read(request, message_id):
#     """Пометить сообщение прочитанным по id сообщения"""

#     message = get_object_or_404(Message, id=message_id)
#     message.is_read = True
#     message.save()
#     return JsonResponse({'Message read': True}, status=200)


# @require_http_methods(['DELETE', ])
# def delete_message(request, message_id):
#     """Удалить сообщение по id сообщения"""

#     message = get_object_or_404(Message, id=message_id)
#     message.delete()
#     return JsonResponse({'deleted': True}, status=200)


# @require_http_methods(["GET", ])
# def chat_info(request, chat_id):
#     chat = get_object_or_404(Chat, id=chat_id)
#     chat_info = {'name': chat.name,
#                  'kind': chat.kind,
#                  'photo': str(chat.photo),
#                  'author': str(chat.author),
#                  'users': [str(user) for user in chat.users.all()]}
#     return JsonResponse({'chat info': chat_info}, status=200)


class ChatsList(generics.ListCreateAPIView):
    """
    Получить список всех чатов +
    Cоздать чат (минимальный набор полей: название, описание)+
    """

    serializer_class = ChatSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Chat.objects.filter(author=user_id)


class ChatDeleteEdit(generics.RetrieveUpdateDestroyAPIView):
    """
    Отредактировать чат по id (минимальный набор полей: название, описание)+
    Удалить чат по id +
    Добавить участника в чат по id челов+
    chat_info
    """

    serializer_class = ChatSerializer
    queryset = Chat.objects.all()


class MessageList(generics.ListCreateAPIView):
    """
    Отправить сообщение по id чата +
    Получить список сообщений по id чата +
    """

    serializer_class = MessageSerializer

    def get_queryset(self):
        chat_id = self.kwargs["chat_id"]
        return Message.objects.filter(chat=chat_id)


class MessageDeleteEdit(generics.RetrieveUpdateDestroyAPIView):
    """
    Удалить сообщение по id сообщения +
    Пометить сообщение прочитанным по id сообщения +
    Отредактировать сообщение по id сообщения +
    """

    serializer_class = MessageSerializer
    queryset = Message.objects.all()
