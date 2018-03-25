
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponse

from chat.models import ChatMessage, ChatRoom

@login_required
def list_chatrooms(request):
  
  data = {}
  
  public_rooms = ChatRoom.objects.filter(is_public=True)
  public = [p for p in public_rooms if request.user in p.users.all()]
  available = [p for p in public_rooms if request.user not in p.users.all()]
  
  private = ChatRoom.objects.filter(is_direct=False, is_public=False)
  direct = ChatRoom.objects.filter(is_direct=True, is_public=False)
  
  private = [p for p in private if request.user in p.users.all()]
  direct = [p for p in direct if request.user in p.users.all()]
  data['public'] = [e.to_dict(request.user) for e in public]
  data['available'] = [e.to_dict(request.user) for e in available]
  data['private'] = [e.to_dict(request.user) for e in private]
  data['direct'] = [e.to_dict(request.user) for e in direct]
  
  data['success'] = True
  return HttpResponse(json.dumps(data))
  
@login_required
def join_public_chatroom(request, chatroom_id):
  chatroom = ChatRoom.objects.get(pk=chatroom_id)
  if chatroom.is_public:
    
    chatroom.users.add(request.user)
    chatroom.save()
    
    return list_chatrooms(request)
  else:
    data = { 'message': "That chatroom is private.", 'success': False }
    return HttpResponse(json.dumps(data), status=401)
    
@login_required
def add_user_to_private_chatroom(request, chatroom_id, other_user_id):
  
  chatroom = ChatRoom.objects.get(pk=chatroom_id)
  
  if chatroom.is_public == False or chatroom.is_direct == True:
    data = {
      'message': "You cannot add that user to that chat.",
      'success': False
    }
    return HttpResponse(json.dumps(data), status=401)
  
  other_user = User.objects.get(pk=other_user_id)
  chatroom.users.add(other_user)
  
  chatroom.save()
  other_user.save()
  
  data = { 'success': True }
  return HttpResponse(json.dumps(data))
  
def create_chatroom(request):
  post_data = json.loads(request.body.decode('utf-8'))
  
  