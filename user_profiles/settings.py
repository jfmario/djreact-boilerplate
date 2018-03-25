
from django.conf import settings

default_main_menu = [
  { 'title': 'Home', 'link': '/' }
]

MAIN_BRAND = getattr(settings, 'MAIN_BRAND', "User Profile Site")
MAIN_MENU = getattr(settings, 'MAIN_MENU', default_main_menu)