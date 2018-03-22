from django.shortcuts import render

# Create your views here.

def site_home(request):
  data = {
    'title': "My Django Site",
    'links': [
      { 'title': 'Home', 'link': '/' },
      { 'title': 'GitHub', 'link': 'https://github.com' }
    ]
  }
  return render(request, 'djreact/home.html', data)