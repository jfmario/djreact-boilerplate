
from django.urls import include, path

from user_profiles.views import edit_profile, view_profile

user_profile_urls = [
  path('profile/<user_id>/view', view_profile),
  path('profile/<user_id>/edit', edit_profile)
]