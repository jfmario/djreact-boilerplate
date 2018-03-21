
# Django-React Boilerplate #

UNDER CONSTRUCTION

This repository should be a little more than a boilerplate for a Django 
project that includes a workspace for building Javascript files for 
the frontend using React.

The plan is to include many tools and utilities that I like, that can be 
easily pruned from projects that don't need particular features.

## Getting Started #

Use this repository for starting Djreact Stack projects.

### Prerequisites #

This assumes that you have Node.js 6+ and Python3.6+.

### Installation #

To get set up, clone this repository and inside of it do the following.

```bash
# install django and other dependencies
pip3 install -r requirements.txt

# migrate database and create admin user
python3 manage.py migrate
python3 manage.py createsuperuser

# set up node_modules
npm i
```

### Usage #

This is a standard Django project with some bells and whistles, see below for 
more info.

All frontend Javascript files should go under `src/`.

## Docs #

* [Django Allauth](https://github.com/pennersr/django-allauth)

This site comes with 
django-allauth
mapped to the url `accounts/`.
It provides a login page, registration page, and redirects logged in users 
as instructed in `djreact/settings.py` (currently, `/`).
See the repo for more details on django-allauth.

* [Allauth Themes](./allauth_themes/)

A theme for the authentication templates,
overriding those provided by django-allauth. To get rid of them,
just remove 'allauth\_themes.bootstrap4' from INSTALLED\_APPS

* [Djreact Utils](./djreact_utils/)

A number of utilities for Django.

## Acknowledgements #

### Authors #

* John F Marion

### Built With #

* Django
* Django-Allauth
* React
* Webpack
