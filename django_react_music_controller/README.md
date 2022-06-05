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

### Creating a Class-Based View (Mode/ View/ Serializer)
- Create Room -- Class(models.Model) in api.models
    - set up fields (name, datatype, constraints and default ..etc)
    - Add function to generate unique room code
        - using models.Model/QuerySet/filter, count
- Update (migrate) database
    - `./manage.py makemigrations`
    - `./manage.py migrate`
- Create a serializerz.py
    - Create app_name/serializers.py
    - Create serializer for Room model -- RoomSerializer
                            (serializers.ModelSerializer)
        - Add serializer Class -- RoomSerializer
        - Add fields to RoomSerializer
- Create class-based view RoomView
        - Assign serializer class to views


## How-To


## References
-
    [Database/Model Migration](https://docs.djangoproject.com/en/4.0/topics/migrations/#:~:text=Migrations%20are%20Django's%20way%20of,problems%20you%20might%20run%20into.)
