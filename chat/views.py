
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from chat import settings

# Create your views here.

@login_required
def chat_home(request):
  data = {
    'brand': settings.MAIN_BRAND,
    'js': 'chat',
    'main_menu': settings.MAIN_MENU,
    'title': 'Chat - {}'.format(settings.MAIN_BRAND)
  }
  return render(request, 'djreact/lit/react.html', data)