from django.urls import path
from chats.views import *


urlpatterns = [
    path('users/<int:user_id>/', ChatsList.as_view()),
    # path('<chat_id>/', MessageList.as_view(), name='chat_detail'),
    # path('create/<int:id>/', create_chat, name='create_chat'), 
    path('<int:pk>/', ChatDeleteEdit.as_view()), 
    # path('add_user_to_chat/<int:pk>/', AddUsrToChat.as_view(), name='add_user_to_chat'), 
    # path('delete_user_from_chat/<int:chat_id>/<int:user_id>/', delete_user_from_chat, name='delete_user_from_chat'), 
    path('chat_messages/<int:chat_id>/', MessageList.as_view()), 
    # path('edit_message/<int:message_id>/', edit_message, name='edit_message'), 
    # path('make_read/<int:message_id>/', make_read, name='make_read'), 
    path('message/<int:pk>/', MessageDeleteEdit.as_view()), 
    # path('chat_info/<int:chat_id>/', chat_info, name='chat_info'), 
]