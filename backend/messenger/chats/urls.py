from django.urls import path
from chats.views import chat_list, create_chat, chat_detail


urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('<chat_id>/', chat_detail, name='chat_detail'),
    path('create/<int:pk>/', create_chat, name='create_chat'), 
]