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

Material UI
Grid
  Grid is used to align things vertically or horizontally
    - spacing{#} is #*8 pixels spacing between items in grid
    - breakpoint (xs, sm, md, lg, and xl) -- " value given to a breakpoint applies to all the other breakpoints wider than it (unless overridden, as you can read later in this page). For example, xs={12} sizes a component to occupy the whole viewport width regardless of its size."
Typography
  - nicely styled/maintained header in material-UI
## Tutorial

### 1. Setting up a Hello World Page

- Install Django
  `pip install django djangorestframework`
- Start Django Project
  `django-admin startproject project_name`
- Put App in Project (folder)
  `django-admin startapp app_name`
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
- Create class-based view RoomView - Assign serializer class to views

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
    - type `doc` + Tab for Emmet Abbreviation of setting up some boilerplate
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

### 4. Component Creation + React Router

- Add index.css to frontend/static/css
- Start configuring index.css
- Edit App.js to render a "prop"

  - "component can render other components" - Tim
  - "props are an attribute/argument that gets passed to the component to modify its behavior" - Tim
  - Adding a prop -- name

    ```
    export default class App extends Component {
        constructor(props) {
            super(props);
        }

        render() {
            return <h1>Testing React Code: {this.props.name}</h1>;
        }
    }

    const appDiv = document.getElementById('app');
    render(<App name="this is a prop" />, appDiv);
    ```

- Component can store "stage", when states are modified react will rerender that whole component -- discussion later on
- Create new component frontend/src/components/HomePage.js
  - don't need the import {render} statement as we plan to render this component from the App.js component
- To show routing, creating another two components RoomJoinPage and CreateRoomPage
- Put all components in a <div> in App.js

```
 render() {
        return (
            <div>
                <HomePage />
                <RoomJoinPage />
                <CreateRoomPage />
            </div>

        );
    }
```

- Router: import components in Homepage instead of putting them in <div>
- Switch is now Routes in react-router v6+
  https://reactrouter.com/docs/en/v6/getting-started/overview
- Need to add routes to Django as well, but can all point to index to let React take over -- THERE's A WAY to AVOID THIS

```
urlpatterns = [
    path('', index),
    path('join', index),
    path('create', index)
]
```

### 5. API View to Create Room on POST

- Import more stuff from rest_framework in views.py of API
- Create a new serializer -- CreateRoomSerializer
  - "whenever you are handling different requests, it's a good idea to create an incoming or outgoing serializer" - Tim
- Import CreateRoomSerializer in views.py and create CreateRoomView(APIView) (class-based view)
- Fix api.models to use generate_unique_code as default of "code" field
- Users won't POST us what the "host" is, instead we want to use a session key -- an established connection between two devices
  - identified by a unique key
  - session will be lost for now if our server crashes
- Draft post() in CreateRoomView to find session
  - does current user have session
  - create session if not

```
~ Random Internet Search ~
What is the difference between forms and serializers? Forms are if you want Django templates to render it out. Serializers if you need a REST API and the frontend can be nearly anything. I got this error here: raise TypeError('view must be a callable or a list/tuple in the case of include().')
```
### 6.  Material UI Components + onChange functions to handle votes/guests-can-pause/room-button
```
"Material Design, which was not asked in the question, is a specification released by Google (as some of these answers correctly state).

Material UI, on the other hand, is a library that uses Facebook’s react framework and exports a set of react components that that follow the principals of Material Design -- Quora"
```
==== UI Changes ====
- Import a bunch of things from material-ui in CreateRoomPage.js
  - http://127.0.0.1:8000/create
- Set default votes value
- Add a Grid Container and a Grid Item (using a max value of xs=12) of Typograhpy
- Add radio buttons using Grid/FormControl/RadioGroup/FormControlLabel 
  - Use FormControlLabel so we can label(name?) our buttons?
- Add number-of-votes text fields with Grid/FormControl/TextField/FormHelperText
- Add button to submit/go-back with Grid/Button
  - Button with component as link and to url for back button
==== Backend Changes ====
- Set this.state of constructor for CreateRoomPage.js
  - "remember when state changes it forces React components to refresh"
  - create handleVotesChange/handleGuestCanPauseChange functions below contructor
- Add onChange attribute to RadioGroup of Play/Pause, NoControl radio buttons
## How-To

## References

- [Database/Model Migration](https://docs.djangoproject.com/en/4.0/topics/migrations/#:~:text=Migrations%20are%20Django's%20way%20of,problems%20you%20might%20run%20into.)
