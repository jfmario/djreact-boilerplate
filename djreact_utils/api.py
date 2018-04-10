
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def is_admin(request):
  if request.user.is_superuser:
    return HttpResponse(json.dumps({ 'is_admin': True }))
  else:
    return HttpResponse(json.dumps({ 'is_admin': False }))