
from django.conf import settings
from django.shortcuts import render

# Create your views here.

def site_home(request):
  data = {
    'title': "My Django Site",
    'links': getattr(settings, 'MAIN_MENU', [])
  }
  return render(request, 'djreact/home.html', data)