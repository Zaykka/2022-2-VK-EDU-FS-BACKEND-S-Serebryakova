import re
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from chats.models import Chat, Message
from users.models import User


@require_http_methods(["GET"])
def chat_list(request, user_pk):
    """Список чатов"""
    chats = []
    user = get_object_or_404(User, id=user_pk)
    for chat in Chat.objects.filter(users=user):
        chats.append({'id': chat.id,
                      'name': chat.name,
                      'kind': chat.kind,
                      'photo': str(chat.photo),
                      'author': str(chat.author)})
    return JsonResponse({'chats': chats})


@require_http_methods(["GET"])
def chat_detail(request, chat_id):
    """Страница чата"""
    messages = []
    chat = get_object_or_404(Chat, id=chat_id)
    for message_meta in Message.objects.filter(chat=chat):
        messages.append(
            {'id': message_meta.id,
            'sent_from': str(message_meta.sent_from),
            'message': message_meta.message,
            'created_at': message_meta.created_at,
            'photo': str(message_meta.photo)})
    return JsonResponse({'chats': messages})


@require_http_methods(["POST"])
def create_chat(request, pk):
    name = request.POST.get("name")
    kind = request.POST.get('kind')
    photo = request.POST.get('photo')
    author = int(request.POST.get('author'))
    users = request.POST.get('users').split()
    author_model = get_object_or_404(User, id=author)
    new_chat = Chat.objects.create(name=name, kind=kind, photo=photo, author=author_model)
    new_chat.save()
    for user in users:
        user_model = get_object_or_404(User, id=user)
        new_chat.users.add(user_model)
    return JsonResponse({'created': True})


@require_http_methods(["POST"])
def edit_chat(request, pk):
    chat_model = get_object_or_404(Chat, id=pk)
    name = request.POST.get("name")
    kind = request.POST.get('kind')
    photo = request.POST.get('photo')
    author = request.POST.get('author')
    users = request.POST.get('users')
    
    if name is not None:
        chat_model.name = name
    if kind is not None:
        chat_model.name = kind
    if photo is not None:
        chat_model.name = photo
    if author is not None:
        author_model = get_object_or_404(User, id=int(author))
        chat_model.author = author_model
    if users is not None:
        for user in users.split():
            user_model = get_object_or_404(User, id=user)
            chat_model.users.add(user_model)
    
    chat_model.save()
    return JsonResponse({'edited': True})

@require_http_methods(["POST"])
def delete_chat(request, pk):
    chat_model = get_object_or_404(Chat, id=pk)
    if chat_model:
        chat_model.delete()
        return JsonResponse({'deleted': True})
    return JsonResponse({'deleted': False})


