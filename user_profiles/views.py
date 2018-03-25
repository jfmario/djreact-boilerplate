
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from user_profiles.models import UserProfile

# Create your views here.

def view_profile(request, user_id):
  
  data = {}
  
  user = getattr(request, 'user', None)
  if user:
    data['user'] = user
    if user.pk == int(user_id):
      data['self_user'] = True
  
  try:
    data['user_profile'] = UserProfile.objects.get(user__id=int(user_id))
  except:
    
    profile_user = User.objects.get(id=int(user_id))
    user_profile = UserProfile(user=profile_user)
    
    user_profile.save()
    data['user_profile'] = user_profile
    
  return render(request, 'user_profiles/profile_view.html', data)