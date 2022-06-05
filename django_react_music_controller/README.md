## Explanation

## Tutorial

### Setting up a Hello World Page
- Install Django
    `pip install django djangorestframework`
- Start Django Project
    `django-admin startproject project_name`
- Put App in Project (folder)
    `djanog-admin startapp app_name`
- Register App
    setting.py.INSTALLED_APPS = [
        ...,
        'app_name.apps.AppAppConfigClassName',
        'rest_framework' # another app needed?
    ]
- Configure Endpoint in views.py
    - Create app_name/urls.py (there's also project_name/urls.py)
    - Project URLs dispatch to App Urls, App Blank URL calls views.main

- Update base on any changes to database/models
    - Or run the first time of initiating app 
    - `./manage.py makemigrations`
    - `./manage.py migrate`
- Run Server
    - `./manage.py runserver`
    (Django server auto reloads the code when you save views)

## How-To


## References
