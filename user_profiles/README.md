
# User Profiles App #

This is a Django app included in the Djreact boilerplate. It supports 
user profiles.

## Usage #

Include `user_profiles` in your installed apps and include the urls in 
`urls.py`:

```python
from user_profiles.urls import user_profile_urls
urlpatterns = [
  # ...
  path('user/', user_profile_urls)
]
```

You do not have to user `user/` as the endpoint.

## Docs #

### Routes #

The route `user/profile/<user_id>/view` will show the profile page where
the Django User's id matches. 

The route `user/profile/<user_id>/edit` will provide a form for editing 
profile page info where the Django User's id matches. A user can only edit his
or her
own profile.

### Models #

**User Profile**

`user_profiles.models.UserProfile`

*Attributes*

| Field | Type | Notes |
| --- | --- | --- |
| `first_name` | CharField | |
| `last_name` | CharField | |
| `image_url` | UrlField | |
| `date_of_birth` | DateField | |
| `gender` | CharField | "M" of "F". From provides a drop down with options. |
| `city` | CharField | |
| `state` | CharField | |
| `country` | CharField | Defaults to "US" |
| `bio` | TextField | |
| `join_date` | DateField | Automatically populated when the UserProfile is created. |
| `user` | ForeignKey to Django User Model | |
| `friends` | ForeignKey to UserProfile | |

## Acknowledgements #

### Authors #

* John F Marion

### Built With #

* Django
