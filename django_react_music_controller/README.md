## Explanation
```
.
├── api                             (app -- api)
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── django_react_music_controller  (django project)
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── frontend                       (app -- frontend)
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   ├── frontend
│   │   └── images
│   ├── templates
│   ├── tests.py
│   └── views.py
├── Makefile                      (commands to run in a terminal that abstracts its underlying calls)
├── manage.py
└── README.md
```

## Tutorial

### 1. Setting up a Hello World Page
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

### 2. Creating a Class-Based View (Mode/ View/ Serializer)
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

### 3. React Integration using Webpack & Babel
- Confirm NPM is installed
- Create new app `frontend` in project
    `make start-app name=frontend`
- Create bunch of folders in new app
    `mkdir templates static`
    `mkdir static/css static/frontend static/images`
    `mkdir frontend/src`
    `mkdir frontend/src/components`
- NPM Initialize in frontend/
    `npm init -y`
- Install Webpack & Babel & React ...etc
    `npm i webpack webpack-cli --save-dev`
    `npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev`
    https://stackoverflow.com/a/53395718/5029381
    `npm i react react-dom --save-dev`
    `npm i @material-ui/core --legacy-peer-deps`
    https://stackoverflow.com/questions/71713111/mui-installation-doesnt-work-with-react-18
    https://docs.npmjs.com/cli/v6/commands/npm-uninstall
    `npm i @babel/plugin-proposal-class-properties` # async/await?
    `npm i react-router-dom`
    `npm i @material-ui/icons`
    https://www.reddit.com/r/reactjs/comments/os126m/why_use_material_ui_what_are_the_benefits/
- Add babel.config.js to frontend/
    https://github.com/techwithtim/Music-Controller-Web-App-Tutorial/blob/main/Tutorial%201%20-%204/frontend/babel.config.json
- Add webpack.config.js to frontend/
- Add script to package.json scripts -- remove "test"
    "dev": "webpack --mode development --watch",
    "build": "webpack --mode production"
- Add index.js to frontend/src
- We want Django to render a page, that React will take control of:
    - Add index.html to frontend/templates
        - Loads static files
        - Load stylesheet css/index.css
        - `App Div for React to render it's components`
        - Load frontend/main.js -- bundled JS so React can take over?
```
When you prepare a React application for production deployment, it gets compiled down into a set of static html, css, and javascript files. Django can serve these production files just like it can serve any other web page, so that’
s no problem.
```
- Create index function in frontend/views.py to request frontend/index.html
    - renders index.html where react takes over
- Create url patterns for 1)controller to see frontend, and 2)frontend to see .views.index
- Add React component -- src/components/App.js to be rendering in App-Div Container
- Run the server / Build the app
    `npm run dev`
- React: Function components are superior compare to class components



## How-To


## References
-
    [Database/Model Migration](https://docs.djangoproject.com/en/4.0/topics/migrations/#:~:text=Migrations%20are%20Django's%20way%20of,problems%20you%20might%20run%20into.)
