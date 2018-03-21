
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

  help = 'Creates and initializes a test game.'

  def handle(self, *args, **options):
    
    user_info = [
      ('applejack', 'orange'),
      ('pinkiePie', 'pink'),
      ('rarity', 'white'),
      ('twilightSparkle', 'purple'),
      ('rainbowDash', 'blue'),
      ('fluttershy', 'yellow')
    ]
    
    for u_info in user_info:
      user = User(username=u_info[0])
      user.set_password(u_info[1])
      user.save()