
from django.urls import include, path

from chat.api import add_user_to_private_chatroom
from chat.api import create_chatroom, create_private_chat, get_recent_messages
from chat.api import leave_chatroom, list_chatrooms, send_message

chat_api_urls = [
  path('create/direct-message/<int:other_user_id>', create_private_chat),
  path('create/room', create_chatroom),
  path('room/<int:chatroom_id>/add-user/<int:other_user_id>',
    add_user_to_private_chatroom),
  path('room/<int:chatroom_id>/leave', leave_chatroom),
  path('room/<int:chatroom_id>/messages/<int:y>/<int:m>/<int:d>/<int:hh>/<int:mm>/<int:ss>',
    get_recent_messages),
  path('room/<int:chatroom_id>/send-message', send_message),
  path('rooms/list', list_chatrooms)
]

chat_urls = [
  path('api/', include(chat_api_urls))  
]