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
Grid is used to align things vertically or horizontally - spacing{#} is #\*8 pixels spacing between items in grid - breakpoint (xs, sm, md, lg, and xl) -- " value given to a breakpoint applies to all the other breakpoints wider than it (unless overridden, as you can read later in this page). For example, xs={12} sizes a component to occupy the whole viewport width regardless of its size."
Typography

- nicely styled/maintained header in material-UI

- [Django Admin](https://docs.djangoproject.com/en/4.1/ref/django-admin/): django admin commands are useful to run many administrative tasks for a Django project, such as:

  `manage.py makemigrations` -- prepare SQL to propagate schema changes, great when you're migrations are up to date and you've made Model changes
  `manage.py migrate` -- apply/unapply (execute SQL to propagate schema changes) migrations, can be used to check if your local is in-sync with latest state of rep
  `manage.py runserver` -- Starts a lightweight development web server on the local machine
  ...etc

You can also [add custom commands to manage.py](https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/)

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

````

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

### 6. Material UI Components + onChange functions to handle votes/guests-can-pause/room-button

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

### 7. /create leads to an actual room/:roomId page

- Create room component -- src/components/Room.js
  - add states of votesToSkip, guestCanPause, and isHost
- Add route/:roomId in HomePage to room/code
  - Use props.match.params.roomId as roomId
  - Add room/<str:roomId> to urlpatterns
- Change class component Room to function component to bypass v6 router issue (no props.match)
  https://stackoverflow.com/questions/69967745/react-router-v6-access-a-url-parameter
  https://reactrouter.com/docs/en/v6/getting-started/tutorial#reading-url-params
  https://reactrouter.com/docs/en/v6/upgrading/reach#update-route-components-to-use-hooks
- Add GetRoom APIView
  - find "code" from request?
  - check if room exist using "code"
  - overide data with host information before returning response
- Add get-room url pattern to api
- Add getRoomDetails function to set state of Room.js <-- need to confirm this is actually working
- Route /api/create-room
  ...
- Summary:
  - Unclear if Router/Route needs to be so many components away from index.js
    - index.js vs index.js -> app.js -> homepage.js
  - Probably better to use function component/react hooks than class components
    - but useful to know how to work around this with a higher order component

### 8. JoinRoom page that navigates to existing room

- Align HomePage to the center
  - and it's children? -- because centering is done on the <div>
- Add RoomJoinPage.js MUI
  - textfield for RoomCode
  - Buttons
- Hook up method CreateRoomPage： handleRoomCodeChange and handleJoinRoomButtonClicked
  - When room is created, now navigates to Room page
- .............. summary ..............
- Get Room always assumes sessions exist, but create/join room needs to check and create sessions, why is this the case?

### 9. something about being about to re-join a joint room is user closes page

- import MUI stuff in HomePage.js to create function that renders what the homepage looks like?
- Create HomePageReal component that shows join/create room buttons linking to /create and /join
- Using a React lifecycle component to help redirect user to a room when they land on a homepage
  - instead of componentDidMount() (class component), achieve the same result with useEffect() in our function component
  - add UserInRoom view: returns room_code of session via JsonResponse
  - add user-in-room path in api.urls
  - set up "redirect" like behavior using Navigate to determine of state.roomCode is set
- .............. summary ..............
  - Use JsonResponse when do not require custom serializer for django models
  - Route element can navigate to another

### 10. Leaving a room

- .............. summary ..............
  - First time we're using a callback function as a prop for a children component to change the state of the parent component (Homepage)
  - Most clear moment why we store room_code in sessions (used to determine user already "joined" a room)
    - Navigate to a room from / (base on checking if that user's session shows it has a room_code)
    - Remove room_code from session when user leaves room

### 11. Creation of a Settings page for host to adjust fields

- create and endpoint for update-room
  - we want to "patch" room, therefore we'd want to deserialize request data into a room object(?)
  - "code" was defined as unique in model so they every room has a unique code, but we want to update the SAME room, therefore we're going to overide the "code" field in UpdateRoomSerializer

### 12. Host can udpate a room

- install material-ui/lab for Alert
- .............. summary ..............
  - Always try to use prop directly from parent, trying to maintain the same state between childre/parent is bad pattern?
    - but using parent.callback in children to "lift state?" up to parent seems okay
  - Used defaultProp and prop expansion in CreateRoomPage.js to do unholy things about reusing component render structure for both Create and Update
  - sx prop not working for repositioning a Snackbar was soul crushing -- hacked with index.css for now

### 13. Check if User is authenticated when entering Room (Spotify API integration)

- create app on [developer.spotify/dashboard](https://developer.spotify.com/dashboard/applications/310822416fcf4ed9a85cfb0a693a002f)
- make new django app for spotify api `make start-app name=spotify`

  - add SpotifyConfig to settings

- set up [spotify authentication flow](https://developer.spotify.com/documentation/general/guides/authorization/code-flow/)

  - credentials.py

    - add client_id, client_secret, redirect_uri
      (for convenience, not good practice vs say storing in environment variables)

  - component

    - Room
      - on entering room, if user is host, then authenticate to spotify?（how about non-hosts?
        - if not authenticated, redirect to spotify auth url (which redirects back if authed)

  - urls.py

    - controller
      - dispatch to spotify.urls
    - frontend
      - for using django.shortcuts.redirect() back to frontend, path needs to be named
        - add app_name = 'frontend'
        - add name='' to path('')
    - spotify
      - add spotify-token-exists/get-spotify-auth-url/redirect end points

  - models.py

    - add SpotifyToken model + make migrations

  - views.py
    - spotify
      - add view: getSpotifyAuthURL (scopes, pypi-requests to prep request url
        - include spotify.urls in controller/urls.py
      - add redirect_from_spotify_auth(view.request)
        - redirect to "frontend:" (named in frontend.urls) after token update/creation
      - add view: spotifyTokenExists
      - util.py
        - is_spotify_authenticated
        - get_user_token
        - refresh_spotify_token
        - update_or_create_user_token
        - create_session_if_missing

- .............. summary ..............
- so far tutorial has interacted with models from views but in this case there's logic in the new utils.py
  - felt like it would be a better idea to have logic in views itself, having to reference util to fix views was pretty annoying

## How-To

- Center a <div> horizontally and vertically
  - use css class <div className='center'>
- [Center NOT a <div> when using MUI](https://medium.com/@tsubasakondo_36683/4-ways-to-center-a-component-in-material-ui-a4bcafe6688e)
  - [One-off override component style](https://mui.com/material-ui/customization/how-to-customize/#the-sx-prop)
- Use JSX element when wanting an arbitrary parent
  - Use Fragment to wrap the JSX element
    - https://reactjs.org/docs/fragments.html

```

.center {
position: absolute;
top: 50%;
left: 50%;
transform: translate(-50%, -50%);
}

```

- [Lifting shared state up](https://reactjs.org/docs/lifting-state-up.html)
- Fetch state to update function component

```

One of the popular cases that using useState inside of useEffect will not cause an infinite loop is when you pass an empty array as a second argument to useEffect like useEffect(() => {....}, []) which means that the effect function should be called once: after the first mount/render only.

````

https://stackoverflow.com/questions/53715465/can-i-set-state-inside-a-useeffect-hook

- Preserve previous state when updating a entry in state
  `setState(state => ({...state, keyToChange: newValue}));`

- [Navigate to another component using a ternary operator (condition)](https://stackoverflow.com/a/70738182/2812257)

- Alter a model's field validation for serializer instance

  - Given "code" is unique, allow a serializer to treat as not unique

  ```python
  class UpdateRoomSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[])  # so code doesn't have to be unique

    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip', 'code')
  ```

```

- ["Run UseEffect()" before render](https://stackoverflow.com/a/56818036/2812257)

- Django: List all values of one field in a model
  - `list(ModelClassName.objects.all().values_list("field_name", flat=True))`

## References

- [React Router](https://reactrouter.com/docs/en/v6/getting-started/concepts)

- Using Function component from Class Component
  https://stackoverflow.com/questions/37516919/react-router-getting-this-props-location-in-child-components
  https://stackoverflow.com/questions/69967745/react-router-v6-access-a-url-parameter
  https://reactrouter.com/docs/en/v6/upgrading/reach#update-route-components-to-use-hooks
  https://reactrouter.com/docs/en/v6/getting-started/tutorial#reading-url-params
  https://www.freecodecamp.org/news/how-to-use-react-router-version-6/

- [React: States and componentDidMount() in function components with Hooks](https://medium.com/@timtan93/states-and-componentdidmount-in-functional-components-with-hooks-cac5484d22ad)

- [Django: Model View Template](https://www.geeksforgeeks.org/django-project-mvt-structure/#:~:text=Django%20is%20based%20on%20MVT,for%20developing%20a%20web%20application.&text=View%3A%20The%20View%20is%20the,CSS%2FJavascript%20and%20Jinja%20files.)
- [Django: Database/Model Migration](https://docs.djangoproject.com/en/4.0/topics/migrations/#:~:text=Migrations%20are%20Django's%20way%20of,problems%20you%20might%20run%20into.)

- [Django: Object Filter vs Get](https://docs.djangoproject.com/en/4.0/topics/db/queries/#retrieving-a-single-object-with-get)

- [Django: What are Sessions](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Sessions)

- [Spotify: Auth Flow](https://developer.spotify.com/documentation/general/guides/authorization/code-flow/)
```
