
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ChatRoom(models.Model):
  
  name = models.CharField(max_length=32, blank=True, null=True, unique=True)
  description = models.TextField(blank=True, null=True)
  is_direct = models.BooleanField(default=False)
  is_public = models.BooleanField(default=True)
  keep_messages = models.BooleanField(default=True)
  users = models.ManyToManyField(User)
  
  def to_dict(self, user):
    return {
      'id': self.pk,
      'name': self.get_name(user),
      'descripton': self.description
    }
    
  def get_name(self, user):
    
    if (not self.is_public) and (not self.is_direct):
      return self.name.replace('_private_', '')
    if (not self.is_public) and self.is_direct:
      for u in self.users.all():
        if u != user:
          return u.username
          
    return self.name
  
  def __str__(self):
    return self.name
  
class ChatMessage(models.Model):
  
  user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_now_add=True)
  text = models.TextField()
  
  def to_dict(self):
    
    data =  {
      'user': self.user.username,
      'timestamp': self.timestamp.strftime('%Y%d%mT%H%M%S'),
      'text': self.text
    }
    
    # optional enrichment with user profile
    try:
      
      from user_profiles.models import UserProfile
      up = UserProfile.objects.get_or_create(user=self.user)[0]
      
      # print(up.image_url)
      
      if up.image_url:
        data['user_image'] = up.image_url
    except:
      pass
    
    return data
  
  def __str__(self):
    return "{} in {}".format(self.user.username, self.room.name)