from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@require_http_methods(["GET"])
def chat_list(request):
    """Список чатов"""
    return JsonResponse({'chats': []})

@require_http_methods(["GET"])
def chat_detail(request, chat_id):
    """Страница чата"""
    return JsonResponse({'chats': chat_id})

@csrf_exempt
@require_http_methods(["POST"])
def create_chat(request, pk):
    """Создание чата"""
    return JsonResponse({'chat_pk': pk})
