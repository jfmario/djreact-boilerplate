
import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from djreact_utils.flash_messages import LitFlashMessage

from user_profiles.models import UserProfile
from user_profiles import settings

# Create your views here.

def view_profile(request, user_id):
  
  data = {}
  data['title'] = settings.MAIN_BRAND
  data['links'] = settings.MAIN_MENU
  
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
  
def edit_profile(request, user_id):
  
  data = {}
  data['title'] = settings.MAIN_BRAND
  data['links'] = settings.MAIN_MENU
  
  user = getattr(request, 'user', None)
  if user:
    data['user'] = user
    if user.pk == int(user_id):
      data['self_user'] = True
      
  user_profile = None
  
  try:
    user_profile = UserProfile.objects.get(user__id=int(user_id))
    data['user_profile'] = user_profile
  except:
    
    profile_user = User.objects.get(id=int(user_id))
    user_profile = UserProfile(user=profile_user)
    
    user_profile.save()
    data['user_profile'] = user_profile
    
  if 'self_user' not in data:
    
    fm = LitFlashMessage("You are not authorized to edit this page.",
      header="Oh No!",
      severity="danger"
    )
    data['flash_messages'] = [fm]
    
    return render(request, 'user_profiles/profile_view.html', data)
    
  if request.method == 'POST' and data['self_user']:
    
    # print(request.POST)
    user_profile.first_name = request.POST['first_name']
    user_profile.last_name = request.POST['last_name']
    user_profile.image_url = request.POST['image_url']
    user_profile.date_of_birth = datetime.datetime.strptime(request.POST['date_of_birth'], '%Y-%m-%d')
    user_profile.gender = request.POST['gender']
    user_profile.city = request.POST['city']
    user_profile.state = request.POST['state']
    user_profile.country = request.POST['country']
    user_profile.bio = request.POST['bio']
    user_profile.save()
    
    fm = LitFlashMessage("Your profile has been successfully updated.",
      header="Great!",
      severity='success'
    )
    data['flash_messages'] = [fm]
    
    return render(request, 'user_profiles/profile_view.html', data)
    
  return render(request, 'user_profiles/profile_edit.html', data)