
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from user_profiles.models import UserProfile

# Create your views here.

def view_profile(request, user_id):
  
  data = {}
  
  user = getattr(request, 'user', None)
  if user:
    data['user'] = user
    if user.pk == user_id:
      data['self_user'] = True
  
  try:
    data['user_profile'] = UserProfile.objects.get(user__id=int(user_id))
  except:
    profile_user = # get user and create something
  return render(request, 'user_profiles/profile_view.html', data)