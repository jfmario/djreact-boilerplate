
import datetime, json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
  
  if chatroom.is_public == True or chatroom.is_direct == True:
    data = {
      'message': "You cannot add that user to that chat.",
      'success': False
    }
    return HttpResponse(json.dumps(data), status=401)
    
  if request.user not in chatroom.users.all():
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

@csrf_exempt
@login_required
def create_chatroom(request):
  
  post_data = json.loads(request.body.decode('utf-8'))
  if ('name' not in post_data) or ('publicity' not in post_data):
    data = {
      'message': "No name or publicity specified.",
      'success': False 
    }
    return HttpResponse(json.dumps(data), status=400)
  if (post_data['publicity'] != 'private') and (post_data['publicity'] != 'public'):
    data = {
      'message': "Invalid publicity.",
      'success': False
    }
    return HttpResponse(json.dumps(data), status=400)
  
  try:
    
    existing_chatroom = None
    if post_data['publicity'] == 'public':
      existing_chatroom = Chatroom.objects.get(name=post_data['name'], is_public=True)
    else:
      existing_chatroom = Chatroom.objects.get(
        name="_private_{}".format(post_data['name']),
        is_public=False
      )
      
    if existing_chatroom:
      data = {
        'message': "Chatroom with that name already exists.",
        'success': False
      }
      return HttpResponse(json.dumps(data), status=400)
  except:
    pass
  
  chatroom_name = post_data['name']
  is_public = True
  if post_data['publicity'] == 'private':
    chatroom_name = "_private_{}".format(post_data['private'])
    is_public = False
    
  chatroom = ChatRoom(name=chatroom_name, is_public=False)
  chatroom.save()
  chatroom.users.add(request.user)
  chatroom.save()
  
  data = {
    'message': "Chatroom created.",
    'success': True
  }
  return HttpResponse(json.dumps(data))
  
@csrf_exempt
@login_required
def create_private_chat(request, other_user_id):
  
  pk = None
  
  other_user = User.objects.get(pk=other_user_id)
  
  try:
    
    existing_private_chats = ChatRoom.objects.filter(is_direct=True, users__id=request.user.pk)
    matches = existing_private_chats.filter(users__id=int(other_user_id))
    
    if len(matches):
      pk = matches[0].pk
  
  except:
    pass
  
  if not pk:
    chatroom = ChatRoom(
      name="d_{}_{}".format(request.user.pk, other_user.pk),
      is_direct=True,
      is_public=False
    )
    chatroom.save()
    chatroom.users.add(request.user)
    chatroom.users.add(other_user)
    chatroom.save()
    pk = chatroom.pk
    
  data = {
    'success': True,
    'id': pk
  }
  return HttpResponse(json.dumps(data))
  
@csrf_exempt
@login_required
def leave_chatroom(request, chatroom_id):

  try:
    chatroom = ChatRoom.objects.get(pk=chatroom_id)
    if request.user in chatroom.users.all():
      chatroom.users.remove(request.user)
      chatroom.save()
  except:
    pass
  
  data = { 'success': True }
  return HttpResponse(json.dumps(data))
  
@csrf_exempt
@login_required
def send_message(request, chatroom_id):
  
  chatroom = ChatRoom.objects.get(pk=chatroom_id)
  if request.user not in chatroom.users.all():
    data = {
      'message': "You do not have permission to post in this room.",
      'success': False
    }
    return HttpResponse(json.dumps(data), status=401)
  
  post_data = json.loads(request.body.decode('utf-8'))
  if 'message' not in post_data:
    data = {
      'message': "No message supplied.",
      'success': False
    }
    return HttpResponse(json.dumps(data), status=400)
  
  message = ChatMessage(
    user=request.user,
    room=chatroom,
    text=post_data['message']
  )
  message.save()
  
  return HttpResponse(json.dumps({ 'success': True }))
  
@csrf_exempt
@login_required
def get_recent_messages(request, chatroom_id, y, m, d, hh, mm, ss):
  
  chatroom = ChatRoom.objects.get(chatroom_id)
  if request.user in chatroom.users.all():
    messages = ChatMessage.objects.get(
      room=chatroom,
      timestamp__date__gte=datetime.date(y, m, d),
      timestamp__time__gte=datetime.time(hh, mm, ss)
    )
    
    data = [m.to_dict() for m in messages]
    return HttpResponse(json.dumps(data))
    
  else:
    data = {
      'message': "You do not have permission to access these messages.",
      'success': False
    }
    return HttpResponse(json.dumps(data), status=401)