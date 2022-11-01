from django.urls import path
from chats.views import *


urlpatterns = [
    path('users/<int:user_pk>', chat_list, name='chat_list'),
    path('<chat_id>/', chat_detail, name='chat_detail'),
    path('create/<int:pk>/', create_chat, name='create_chat'), 
    path('edit/<int:pk>/', edit_chat, name='edit_chat'), 
    path('delete/<int:pk>/', delete_chat, name='delete_chat'), 
]