
from django.urls import include, path

from user_profiles.views import view_profile

user_profile_urls = [
  path('profile/<user_id>/view', view_profile)
]