<<<<<<< HEAD:not_quiz/dev_notes.py


Sharecode?
https://gist.github.com/

ChatRoom:

BootCamp
https://gitter.im/Colt/TheWebDeveloperBootcamp

CodeTalk
https://gitter.im/Colt/WDB-CodeTalk

JobTalk
https://gitter.im/Colt/WDB-Jobs


Syllabus:
1-18: front end
19-end: back end

course_slides:
https://drive.google.com/drive/folders/0B7qHXcyKO8LKWGdpcXQtM2liUjQ


requests
static/dynamic pages

HTML - structure (noun) -HyperText Markup Language
CSS - skin (adj) -Cascading Style Sheets
JavaScript - actions (verb)

sample: https://codepen.io/Colt/pen/WQQVvE
        https://codepen.io/anon/pen/GmYwrY (alan refactored)


sublime short cuts:
    html + tab gives html structure



###Intro to HTML:
- write properly structured html
- write closing/self-closing tags
- recreate simple website base on photo


elements: block/inline

lorem + tab (in html) to get random block text

generic containers:
    div - block
    span - inline

attributes:
    <a href=""></a>
    <img src="">



###Intermediate HTML:
-write valid html table
-write valid html forms using <form> <input> <select> <label>

html table
html form



###Intro to CSS:
-general rule of css
-correctly include css in html
-select elements by tag name, class and ID
-style elements with basic properties
-using chrome inspector tool to debug html/css

CSS samples:      http://www.csszengarden.com/
CSS color names:  http://colours.neilorangepeel.com/

General Rule：
selector{
    property: value;
    anotherProperty: value;
}

-can style via tag attributes
-can style via style tags (css sytax)
-ultimately style via link tag + separate .css file

Properties:
    Coloring:
        names (147 choices)
        color: red

        hexadecimal color:  0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
        color: #_ _ (R) _ _ (G) _ _ (B)

        rgb: each 0-255
        color: rgb(r, g, b)

        rgba: adds alpha ( 0.0-1.0 )
        color: rgba(r, g, b, a)

    Background:
        background: color
        background: url("http://blah.jpg")
        background-repeat: no-repeat;
        background-size: cover

    Border:
        border-color: purple;
        border-wide: 5px;
        border-style: solid;

        border: 5px solid purple;

    Text Decoration:
        text-decoration: line-through;

    float: left/right..etc (pulls element out of doc flow and floats it in a direction
        until it touches the border of the "containing box" or another floating element)

Selectors:
#https://code.tutsplus.com/tutorials/the-30-css-selectors-you-must-memorize--net-16048
#( but not really )
    #sharing attribute
    selector1, selector2 {
        attribute
    }


    element:
        element { }

    id:
        <p id="blah">
        "This attribute assigns a name to an element. This name must be unique in a document"
        #id_name { }

    class:
        <p class="blah">
        .class_name { }

        # class="A B" (multiple classes A and B)

    star: "applies to everything?"
        * { }

    combinators:
    descendent selector: "can be chained with other elements/selectors"
        li a { }  "any anchor tag inside an li"
        ul li .blah { }


    adjacent selector: "apply property to tags right after (not within) the parent"
        h1 + ul { blah }  "blah applied to ul(s) after all h1(s)"
    child selector:
        div:nth-of-type(3) > p {} "all p  inside third div"


    attribute selector: "apply property to tags with said attribute"
        a[href="http://blah"] { blah } "blah applied to all anchors with href blah"

        input[type="text"] { blah }

    nth of type:
        ul:nth-of-type(3) { blah } "apply property blah to every third ul"
        li:nth-of-type(3) { blah } "applies blah to the 'only third' li in each ol/ul (an ul with 6 li don't get blah applied twice "
        li:nth-of-type(3n) { blah } "same as above but repeated applies to every third"
        li:nth-of-type(even) { blah } "applies blah to EVERY 2nd li (multiple occurence in same ul/ol"

    pseudo class "specific state of class (hover, checked, visited"

    pseudo element "specific part of the element (first letter)"

Specificity:
    "selectors step over each other and the most specific one gets applied"

    "from least powerful to most powerful (in multiple power of 10s":

        #type selectors
            h1 + ul more powerful than h1
        #class , attribute, pseudo class selectors
            .hello{}
            input[type='text'] {}
            a:hover / input:checked
        #id selectors
            #hello



###Intermediate CSS:
- manipulate common font and text properties using css
- include external fonts using Google Fonts
- define and manipulate the four components of the Box Model

p {
    font-family: Arial;   # quotes needed if not one word
    font-size: 200px;
    font-size: 2.0em; #dynamic sizing (in this case double of parent)
               2.0rem; #rem is relative to html (root) font-size
    font-weight: bold; 100/200-800 (some fonts only);
    line-height: 2; #line spacing multiple base on font size
    text-align: right;center;
    text-decoration: underline;/line-through;
}


Google fonts: https://fonts.google.com/
-can find embedded links that can be used in your <head> (before your own css link <- optional or not?)
-dont select more font weights than you need as it adds page load time

HTML: <link href="https://fonts.googleapis.com/css?family=Lemonada" rel="stylesheet">
CSS : p { font-family: Lemonada; }


The Box Model:
- each element is represented as a rectangular box with four edges: margin edge, border edge, padding edge, content edge

p {
    border: 2px solid blue;
    padding: 10px;
    padding-left; 10px;
    margin: 50px;
    margin-top; 50px;
    margin: top right bottom left;
    margin: top/bottom right/left;   <-?
    margin top auto right auto; <- confirm what auto does
    0 dont need px
}



###Bootstrap:
- define bootstrap and explain why we use it (library)
- include bootstrap locally (download) and by using a CDN
- use common bootstrap components like navs and buttons
- build layout using bootstrap grid system

http://getbootstrap.com/

http://expo.getbootstrap.com/ #see how bootstrap is being used

bootstrap classes:
jumbotron (div - makes items within div a jumbotron)
container (div - place items with div in a margin-ed container)
form-group (div -makes grouped items closer to each other)
form-control (input -style and place inputs under labels)
form-inline (form - make items in form display in a line)

http://getbootstrap.com/components/#navbar

nav- navbar navbar-default
div - navbar-header
a - navbar-brand
div - collapse navbar-collapse
ul - nav navbar-nav
ul - nav navbar-nav navbar-right

the grid system: (12 column)
- has to be in a "container" class
- set size for parents: (example shows lg does not need to be set if you want it to be
    3 as well)
    <div> class="col-md-3 pink">col lg 3</div>
- four sizes: lg, md, sm, xs
- use class="row" for nesting grid
- use div-class="thumbnail" to constrain image size (this may not just work the way you want when you have various image sizes)
https://www.udemy.com/the-web-developer-bootcamp/learn/v4/t/lecture/6195846?start=0

    ~~ Alan on padding vs margin: ~~
    rule of thumb is "who is responsible", the parent or child
If you want spacing around your children, then padding on the parent...
if each element needs to space themselves, it is margin

- sometimes you will have to use inspector to find the selector thats having the effect on the style and use it to add the override you need (Specificity conflicts)

- bootstrap comes with usable icons:
    Glyphicons
- for more options theres also a bunch of icons available at fontsawesome:
    font awesome
    https://www.bootstrapcdn.com/fontawesome/
    http://fontawesome.io/icon/shower/



###Into to JS:
- evaluate js in chrome dev console
- 5 js primitives
- define use variables (var keyword)
- use built-in methods console.log, alert, prompt

variable declartion:
var var_name = var_value;

variable naming:
favors camelCase

undefined:
var defined but never given a value

null:
var defined explicitly as empty/nothingness


some built-in methods:
alert(value):
    an annoying print

console.log(value):
    print

prompt(value):
    prompt with "value", does return the entered value therefore can store
    as another var



###JS control flow:
- evaluate logical expressions
- 3-part conditional statements
- while/for loops
- translate between while/for loops

boolean:

== (5 == "5" is true)
=== (equal value and type, 5 === "5" is false)
!== (not equal value or equal type, 5 !== "5" is true)

type coercion for ==

99 == "99" true
99 === "999" false

null == undefined true
null === undefind false

logical operators:

&& AND, || OR, ! NOT

falsy values:
false, 0, "", null, undefind, NaN

conditionals:

if(condition) {doSomething}
else if(condition) {doSomething}
else {doSomething}

if() {
    doSomething;
} else {
    doSomething;
}

loops:
#DRY (dont repeat yourself)

while(condition) {doSomething}

for(var init; condition; step) {doSomething}

for(let variable of iterable) {doSomething}


###JS basic functions:
-function declarations, function expressions
-console.log vs return
-define functions to take multiple arguments
-scope, higher functions

function functionName() {}
functionName();

in JS if an arg is not given it is just taken as an undefined, instead of giving
errors.


example with built-in methods:

#function declaration
function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}


#function expression (can later override what capitalize is)
var capitalize = function(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}


scope (the context that code is executed in)

'''thats what var is for without any qualifier, a variable declared in a
   function takes global scope. if you declare test as var test in the
   function, it wont overwrite the test outside '''

Higher Order functions
#take(as arg) or return a function

setInterval(function, millisecond) #returns a number

clearInterval(provide_returned_number_here_to_stop)

#anonymous function
function() {doSomething}



###JS arrays
- define and add data to arrays
- utilize built-in array methods
- console todo list

var arrayName = [blah, blah, blah];

#can assign directly to none existant index to grow array?
arrayName[4] = blah;

arrayName => [blah, blah, undefined x 1, blah]

var arrayName = [];
var arrayName = newArray(); #uncommon

array methods:
push/pop
shift/unshift
indexOf
slice

push: like python append but also returns length of array

unshift: add to front of array and return legnth of array
#array.insert(0, item)  item_array_ref.extend(array) in python?

shift: remove first item in array and return the removed item
# del array[0] in python?


var blah = "abcd"

blah.indexOf("a") => 0
blah.indexOf("e") => -1

#python blah.index("a")

slice: slice(start(gets included), end(not included))
[1,2,3].slice(1,2) => [2]  #python [1,2,3][1:2]

list.slice() #make a copy


#array iteration

array.forEach(someFunction)
# whether feeding a function or an anonymous function forEach by default expects
# arguments of ( item_per_items, index_item, items(array) )

# arr.forEach(function callback(currentValue, index, array) {
#     //your iterator
# }[, thisArg]);

# remove an item of item_index from array ONCE(?)
array.splice(index_to_delete, 1);
    # filter a very good option as well as it actually can return an array without the item (instead of an array of the removed items)
    # https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter

# for testing uniform in array consider array.every()
# https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every

#creating arrays
Array.from({ length: 5 }, (_, i) => i);
// => [0, 1, 2, 3, 4]

Array.from(Array(20).keys())
// => [0, 1, ..., 20]
#Array.from(Array(20).keys()).map(i => i + 1)   <= goes till 20


#arrow function syntax
() => {}
is equiv to
function() {}


###JS objects (key-value pairs)

#unlike arrays, objects have no order
    #don't need string keys like in python dictionary

#initialize object
1)
    var something = {};
2)
    var something = {
        key1: value,
        key2: value2
    };
3)
    var something = new Object();

#value retrieval
something["key1"] => value
something.key1 => value
    # dot notation limits: can't access key starting with number, with spacing

#js methods
#add method to object
#good for avoiding namspacing colliding
    #(same method names in diff object no collision)

a property inside an object hat is a function as a "method"

var something = {};

something.printStuff = function(stuff){
    console.log(stuff)
}

#`this` keyword

var something = {};
something.toPrint = [1,2,3];

#in here this refers to something, "this" will behave different in
#DIFFERENT CONTEXT
something.printStuff = function(){
    console.log(this.toPrint);
};



### DOM manipulation
- define what DOM is
- examples of sites using js to manipulate DOM
- understand SELECT, MANIPULATE workflow

'''
games, scrolling effects, dropdown menus, form validations
iteractivity, animations '''


http://patatap.com/


#document object model: interface between js and html+css

#warning console.dir(object) is a non-standard feature
console.dir(document) reveals the document object

#select and manipulate
#changing color to pink for h1
var h1 = document.querySelector("h1");
hi.style.color = "pink";

# five dom SELECTION methods
document.getElementByID()
# getElementsByClassName() returns an object (of objects) Nodelist?
# that's not quite an array (no forEach method..etc)
document.getElementsByClassName()
document.getElementsByTagName()

# querySelector methods pretty much replaces all getElement methods?
# querySelector() returns first element that matches css-style selector
document.querySelector("ul li")
document.querySelectorAll()

# MANIPULATION
- changing element style
- add/remove classes
- changing content of tag
- changing attributes (src, href)

# manipulate STYLE one at a time
var tag = document.getElementByID("blah"); #select

tag.style.color = "blue";                  #manipulate
tag.style.border = "10px solid red";
tag.style.fontSize = "70px";

# above is too repetitive (not DRY), need to have "separation of concerns"
# solution/alternative: define a new class then turn it on or off via js

# css
.some-class {
    color: blue;
    border: 10px solid red;
    fontSize: 79px;
}

# read-only property, not an array (probably really means don't support forEach)
tag.classList.add("some-class")
             .remove
             .toggle #also returns true/false

# manipulate text CONTENT
<p>This is <strong>blah</strong> boo</p>

var para = document.querySelector("p");
para.textContent #"This is blah boo"  <- doesn't show html tags
para.textContent = "boo boo boo"; # warning: this will not preserve origin html
                                  #          tags (such as strong)
para.innerHTML # "This is <strong>blah</strong> boo" <- shows html tags

para.innerHTML = "<strong> boo boo boo</strong>" # html will take effect, but
                                                 # no effect if assigned by
                                                 # textContent

# manipulate attributes
<a href="blah.com">Im blah link</a>
<img src="blah.png">

var link  = document.querySelector("a");
link.getAttribute("href"); #"blah.com"
link.setAttribute("href", "boo.com");

var img = document.querySelector("img");
img.setAttribute("src", "booo.png");



### advanced dom manipulation

# events
# clicking button / drag and drop / keypress / hovering over link

# add event listener to selected elements
element.addEventListener(type, functionToCall);

# another way to use `this`
# in this case `this` represents lis[i]
for(var i =  0; i < lis.length; i++){
    lis[i].addEventListener("click", function(){
        this.style.color = "pink";
        });
}

#https://developer.mozilla.org/en-US/docs/Web/Events
hover example: mouseover / mouseout

#irrelevant but interesting: wayback machine: https://web.archive.org/

use style.backgroundColor instead of style.background (doesnt work in firefox?)

# https://jsperf.com/concat-vs-plus-vs-join
string concatenation is fast in js? (not part of lecture)



''' FIXES to fix for number game  michael chen mchen
Object.keys(pScores).forEach(function(pKey, index){
Object.keys doesnt necessarily return the keys of your object in the order you wrote them
its the same thing as getting the keys of a python dictionary
a more unified way to do this is replace var pScores = {p1: 0, p2: 0}; with a more complex object that stores the scores as well as the p1count/p2count elements
like `var pState = {p1: {score: 0, element: p1Count}. p2: {score: 0, element: p2Count}}
var pState = {p1: {score: 0, element: p1Count}. p2: {score: 0, element: p2Count}}
var pState = {p1: {score: 0, element: p1Count}, p2: {score: 0, element: p2Count}}
and then just update this state
'''



### intro to jquery
-dom manipulation library
    - select/manipulate/create/animate elements
    - add event listener / effects
    - make http requests (ajax)
http://youmightnotneedjquery.com/

#previous reasons for using jquery:
    - fixes "broken" DOM api
    - brevity/clarity
    -cross-browser support
    -ajax
    -popular
#why not use jquery
    - DOM api no longer "broken"
    - doesn't do anything you can't do on your own
    - its an unnecessary dependency
    - performance
    - no longer popular

#adding jquery
- cdn: https://code.jquery.com/
- or local script text/JavaScript src it

check link by typing jQuery or $(a function) in console

# Ian note  In order to view the element you must access it via $('div')[0];
# https://stackoverflow.com/questions/13552432/show-elements-when-logging-jquery-object-in-chrome-dev-tools-console/13567689#13567689

#jquery selectors
$("selector") #returns ALL matching elements (a list even if one item)
$(".class")
$("#id")
$("li a")
    #first/last
    $().first(), $().last()

#manipulating style of all selected (don't need a new for loop)
$().css(property, value/object)
$("#blah").css("border", "2px solid red")

var styles = {
    color: "red",
    background: "pink",
    border: "2px solid purple"
}

$("#blah").css("border", styles)

$("#blah").css("border", {
    color: "red",
    background: "pink",
    border: "2px solid purple"
})

# jQuery methods

# val()
note: same discription as attr() but for getting/setting value
on input, select, textarea..etc

# text()
'Get the combined text contents of each element in the set of matched elements, including their descendants, or set the text contents of the matched elements.'
note: cant be used to set html

# attr()
'Get the value of an attribute for the first element in the set of matched elements or set one or more attributes for every matched element.'
note: similiar to .css() can feed in an object to set multiple attributes at once

# html()
'Get the HTML contents of the first element in the set of matched elements or set the HTML contents of every matched element.'

# addClass()
# removeClass()
# toggleClass()
    ~classList.methods() without the need of loops



### advanced jQuery

# events (most common)

# on() (MOST MOST COMMON?)
 - similar to addEventListener in which it lets you specify
the type of even to listen for

 - pretty much can use this for all events?

 - click() only adds listener for existing elements

 - on() will add listeners for all potential future elements(
    selector flag NEED TO BE specificed)
    .on( events [, selector ] [, data ], handler )
    # selector being a descendant of the element selected for on()


# click()
    # need to use jQuery version of "this" when "this" is desired
$().click(function {
    doSomething;
    $(this).css.(something)
    })

# keyPress()
the key pressed (shift + a ---> A)

    #getting the key pressed
    # event.which returns the key code http://keycode.info/
    keyPress(function(event/e){
        console.log(event.which)
        });


# jQuery effects
# https://api.jquery.com/category/effects/

# fadeOut
# http://api.jquery.com/fadeout/
# 'fast' and 'slow' can be supplied to indicate durations of 200 and 600 milliseconds, default being 400

.fadeOut( [duration ] [, complete ] )

note:
    - code does not wait for fadeOut to complete to run, therefore if
        that is the desired behaviour you should use a callback function
    for the [, complete] argument
    - fadeout turns diplay to none and does not remove html like
        $().remove() does


.fadeToggle() : similiar to classList.toggle for fadeOut/fadeIn

# slide: animates height, down to show up and up to go away
.slideDown / slideUp / slideToggle



### todo list  projects   jquery + html + css
- jquery: new methods, parent(), append(), creating elements,
    event delegation

- css: fontawesome, box shadow, transition , gradient


# event bubbling event.stopProgpation()
when you activate an event within parents/containers, the event can keep
firing up until it hits <html>, ex: a click event on body and a button in
body, clicking the button would trigger the button event, BUT also the body
event (body is treated as being clicked as well)

if this is undesirable the "event" object should be passed in the click
function and you can call event.stopProgpation()


# gradient
https://uigradients.com/



### patatap clone
- more exposure to third party libaries: paper.js, howler.js

# telling paperscript what id to look for(="canvas") for canvas
<script type="text/paperscript" canvas="canvas">


# l196 note:
'''
include paperscript code internally using script tag, if included as external
.js file it will break the app due to "cross origin resource sharing"

https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS
'''

# used paper.js for canvas operations, holwer.js for playing sounds



### intro to backend
- review internet basics, static vs dynamic sites, stacks/back end tech

www.udemy.com -> 23.234.47.175

# finding the right address
- query submitted to isp, within isp, the DNS takes the domain name and turns it into ip address

# going to that address
- request sent to desired ip via HTTP, finds fastest path to server with specified ip, requires hoping around servers

# udemy server responds
- requested server figures out what we are asking for, server builds right content (often pulling info from database), server responds with any combination of html, css and js

# static vs dynamic
- static sites always give you the same html, css, and js


# stacks
- see what stack companies use: https://stackshare.io/


# http requests
postman chrome app (good for debugging)

various http verbs (get (retrieval), post(add/submit usually via form) ..etc)

3 components of a response:
- body (content,pages source to be rendered into a web page?)
- header (meta data about the response: content type, date, time, status )
- status code(number that represents the response)


get request can still feed in some inputs via query string (?q=blah&haha=meh)



### the command line

# all cloud9 solutions for bootcamp
https://ide.c9.io/learnwithcolt/webdevbootcamp


https://www.davidbaumgold.com/tutorials/command-line/

ls, cd, mkdir, touch, rm , rm -rf
# most of these you can do multiple operations at once with a space between the inputs



### node js

what is node:
    what we use to run js on the server side


node "filename.js" # running a .js file


# what is npm: (latest movement is to use yarn?)
    - package manager for js

# why npm is good:
    - easy to use "npm install"

# packages we will be using:
    - mongoose, express, faker (exercise)

    - install package in the same directory as the file that is calling it (probably ways around this)

    - require() to include package :
      var faker = require('faker');



### server side frameworks

# what is a framework, how is it different from a library?
    - inversion of control, the framework calls you (vesus you call a library)
    - set ups where you fill in the predefined blank space

# what is express?
    - node web dev framework

# why are we using express?
    - light weight framework (vs rails is heavier)
        - more do it yourself (more blank space to fill vs less)


# routes
    - code that are responsible for receiving/lisetning requests, and deciding
      what to send back


# running the server
# node app.js -> preview running app
cloud 9 repo - https://ide.c9.io/lucidsushi/webdevbootcamp


# explain `--save` flag to install packages
'''`npm install <pkg> --save` afterwards to install a package and
save it as a dependency in the package.json file`'''

install multiple at once with `npm install <pkg1> <pkg2> --save

# explain package.json does
meta data which also includes what other packages are needed for it to run
(instead of including all the actual ingridients, give a list of ingridients)

# use `npm init` to create a new package.json

 '''
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

'''

# npm check package
npm list --depth=0 | grep package_name
npm ls package_name


# `*` route matcher will make everything
# route order matters, nothing else will get matched if * goes first
app.get("*", function(req, res) {
    res.send("You are a STAR!");
})

# routes containing route parameters/variables
# which makes the path not "hard coded"
prepend the param/var with a ":"

app.get("r/:something/blah/:boo");

can be queried via req.params => req.params.something // req.params.boo


# route order
further app.get() will not run when one is matched (kind of like elif statements)


# listen for requests (start server)
'''
// *** tell express to listen for requests (start server) ***
// need to use process.env.PORT (returns a number) for cloud9 instead of a direct number
// (os.environ['PORT'] in python)
app.listen(process.env.PORT, process.env.IP, function(){
    console.log("Server has started!!");
});
'''


### Intermediate express

# new tip: `c9 app.js` to open the file in editor on cloud 9
- express looks in "views" folder (not an arbitrary foldler name) for ejs

# use res.render() to render html from EJS file
feeding variable to ejs via objects:
    var name_in_current_scope = req.params.thing;
    res.render("love.ejs", {name_in_ejs: name_in_current_scope});

# what/why EJS https://www.npmjs.com/package/ejs
npm install ejs --save

# pass variable to EJS template
assign the special brackets + some var name =>  <%= varName %>
<h1>you fell in love with: <%= thingVar %></h1>
<%= thingVar.toUpperCase() %> #js methods support within brackets

code within brackets is treated as js code, then the return is passed to html

# ejs control flow
Escaped output with <%= %> (escape function configurable)
Control flow with <% %>

# styles and partials
- include public assets / serve public style sheet
  (images, CSS files, and JavaScript files)
    # https://expressjs.com/en/starter/static-files.html
    # tell express to serve the content of the "public" directory

    app.use(express.static("public"));
    app.use(express.static(__dirname + "/public")) #safer alternative

- configurate app to use ejs
    app.set("view engine", "ejs");# now no longer need to  put .ext for file
                                  # name inputs to res.render("file")
- use partial to dry up code
    -"partial" is a generic name
    - removes the need to repeatedly created the same html tag structure for each
      file in views
    - mkdir partials in 'views' folder
    - create header/footer.ejs files (the html from start to <body> being header,
                                      the html from </body> to </html> being footer)

    - for files in views add include statements at top and bottom:
        <% include partials/header %>
        <% include partials/footer %>

# post requests
- write post routes, test with postman
    app.post("/route", function)

- use a form to send post request
    <form action="/addfriend" method="post">

- use body parser to get form data
    'Parse incoming request bodies in a middleware (req.body?) before your'
    'handlers, available under the req.body property.'
    https://www.npmjs.com/package/body-parser
    npm install body-parser --save

    var bodyParser = require('body-parser');

    // This object will contain key-value pairs, where the value can be a string or
    //  array (when extended is false), or any type (when extended is true).
    app.use(bodyParser.urlencoded({ extended: true }));

    formData = req.body.name_of_input_in_form



### Working with APIs
# application programing interface
https://ifttt.com/
https://www.programmableweb.com/
- wep apis usually accessed through http requests
- make http request to api -> get some data back

# xml /json
xml - extended markup language - syntacticly similar to HTML, but does
not describe presentation like HTML does (ex: bold, strong)

json viewer chrome:
    https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh
    or http://jsonviewer.stack.hu/

# making api requests with node
- making requests in command-line using curl https://tldr.ostera.io/curl
- making requests in node using 'request': https://github.com/request/request

# %20 is how you encode "space" in an url

returned body could be just a string, therefore recast it to an objecting using:
    parseData = JSON.parse(body);

# using api key for request..
request vs request&apikey=thewdb



### Yelp Camp Basics
- add landing page
- add campground page that lists all campgrounds

    each campground has:
        -name
        -image

- create header/footer partials
- add bootstrap

- creating new campgrounds
    - setup new campground POST route
        share the same route name as get route to match REST convention/req
    - add in body parser
    - setup route to show form
    - add basic unstyle form

- style campground page
    - add better header/title
        - use double bootstrap containers as a trick to get the inner text to
          maintain some sort of padding when the page is shrunk in
    - make campgrounds display in a grid
        - <div class="row text-center" style="display: flex; flex-wrap: wrap;">
            - flex styling options used to make non-uniform images fit nicely

- style the navbar and formsomehow renaming a local folder doesnt break the git repo, any idea how this works?


1 /path/folder_name (master)

2 renames folder_name

3 /path/new_folder_name (master)
i want to rename the folder name, but not affect the repository in any way, like pull/push..etc
    - add navbar to all template

    - style new campground form
        - use bootstrap built-in <div class="form-group"> to put some vertical
        spacing between inputs



### databases

# intro to databases
- what is a database
    - collection of information/data
    - has an interface to interact with (db.dogs.find())
- sql (relational) vs. nosql (non-relational)
    - sql: tables, join tables, less flexible (new attributes need to be
        applied to all table entries)

    - nosql: dont need tables (doesnt mean its better than sql), more flexible

- what is mongodb (nosql)

- installing mongodb on c9
    - https://community.c9.io/t/setting-up-mongodb/1717

    - reparing mongo crash (if left running and timed out)
        cd ~
        ./mongod --repair

        # if still doesnt work
        cd ~/data
        rm mogod.lock
        cd
        ./mongod

-mongo commands
    # CRUD create/read/update/delete
    -mongod
        - starts the mongo daemon (process)
        # start it and leave it running in its own tab
    -mongo
        - launches mongodb shell
    -help
    -show dbs

    -use (sets current database or create it if it does not exist)
    -show collections (show collections in db)

    # below probably most important
    -insert
        - db.collection.insert(object)
            # unique "_id": ObjectId("") gets assigned by mongodb
    -find
        - db.collection.find() # shows the whole collection
        - db.collection.find(object) # shows entries matching object
    -update
        - db.collection.update(object_to_select, object_to_update)
            # this wipes out all other keys in the object
        - db.collection.update(object_to_select, {$set: object_to_update})
            # this will not wipe out keys not in original object that is not in
            # object to update
        - db.collection.update(object_to_select, {$set: object_to_update}, {
            multi: true})
            # additional extra flags exist to support certain operations, in
            # this case 'multi' needs to be set to true to actually update more
            # than one
    -remove
        - db.collection.remove({}) #removes everything
        - db.collection.remove(object_to_select) # removes all matching
        - db.collection.remove(object_to_select, {justOne: true}) # removes 1 match

# TODO (look into database migration)
# changing the db schema, like adding a property, and then looping through
# existing rows to update them all is called database migration.
# if you google mongodb db migration might help ya out


# intro to mongoose
    object data maper, object modeling tool (js layer on top of mongodb)

# some potential warnings
    ''' # 1
    Mongoose: mpromise (mongoose's default promise library) is deprecated,
    plug in your own promise library instead:
    http://mongoosejs.com/docs/promises.html
    '''
    # solution (after requiring mongoose):
    # replace mongoose's default promise library with js' native promise lib
    mongoose.Promise = global.Promise;


    ''' # 2
    `open()` is deprecated in mongoose >= 4.11.0, use `openUri()` instead,
    or set the `useMongoClient` option if using `connect()`
    or `createConnection()`
    '''
    # solution (instead of the regular mongoose.connect() syntax)
    mongoose.connect("mongodb://localhost/yelp_camp", {useMongoClient: true});

# using mongoose
    - elegant mongodb object modeling for node.js


    # creating schema
    const catSchema = new mongoose.Schema({
    name: String,
    age: Number,
    temperament: String
    });


    # compile to model (returns an object with useful methods)
    const Cat = mongoose.model("Cat", catSchema);
    "Cat" is the 'singular' version of the model, and collection 'Cats' gets
    created if it does not exist (always feed in singular, and it creates
        the plural somehow?)


    # add data to db
    # method 1
    const george = new Cat({
        name: "SushiCat",
        age: 2,
        temperament: "Tasty"
    });

    george.save(function(err, cat){
        if(err){
            console.log("something went wrong");
        } else {
            console.log("we just saved a cat to the db:");
            console.log(cat);
        }
    });

    # method 2
    Cat.create({
    name: "Angerrr",
    age: 10,
    temperament: "Pissed"
    }, function(err, cat){
        if(err){
            console.log(err);
        } else {
            console.log(cat);
        }
    });


    # retrieve all cats
    Cat.find({}, function(err, cats){
        if(err){
            console.log("oh no, ERROR");
            console.log(err);
        } else {
            console.log("all the cats....");
            console.log(cats);
        }
    });



### yelpcamp: data persistence
-install/configurate mongoose
-setup up campground model
-use camground model inside of our routes

'''random note
https://stackoverflow.com/questions/694102/declaring-multiple-variables-in-javascript
'''

# show page
- RESTful routes / rest table

name    url             verb    description                  mongoose
==========================================================================
INDEX   /dogs           GET     Display a list of dog        Dog.find()
NEW     /dogs/new       GET     show new form                N/A
CREATE  /dogs           POST    Add new dog to DB, redirect  Dog.create()
SHOW    /dogs/:id       GET     Shows info about one dog     Dog.findById()
EDIT    /dogs/:id/edit  GET     show edit form for one dog   Dog.findById()
UPDATE  /dogs/:id       PUT     update the dog, redirect     Dog.findByIdAndUpdate()
DESTROY /dogs/:id       DELETE  delete the dog, redirect     Dog.findByIdAndRemove()

# where in our examples update/destory use "post" by default, and method-override
# to correct verbs put/delete

# https://expressjs.com/en/guide/routing.html
# recall that /:parameter is convention for route parameters in express

- add description to campground model
- show db.collection.drop()
    returns true when successfully drops a collection (removes collection)
- add a show route/template



### RESTful routing
# Representational state transfer (REST)
REST - a mapping between HTTP routes and CRUD

# RESTful routes
https://gist.github.com/alexpchin/09939db6f81d654af06b

# blog index
- setup blog app
    ''' general app.js set up recap

    const express       = require("express"),
          mongoose      = require("mongoose"),
          bodyParser    = require("body-parser"),
          app           = express();

    // app config
    mongoose.connect("mongodb://localhost/yelp_camp", {useMongoClient: true});
    mongoose.Promise = global.Promise;
    app.use(bodyParser.urlencoded({extended: true}));
    app.use(express.static("public"));
    app.set("view engine", "ejs");


    app.listen(process.env.PORT, process.env.IP, function(){
        console.log("app.js running");
    });

    '''
- create the blog model
    - introduction to default value in mongoose schema:
        ex: "created: {type: Date, default: Date.now}," vs "created: Date,"
- add INDEX route and template

# basic layout
- add header/footer partials
- include semantic ui
    - similar to bootstrap + also has a bunch of icons (like fontawesome)
- add simple nav
    - served public asset app.css to enlarge icon (very specific selector to
        overcome libarys specificity)

# putting in the C in CRUD
- add NEW route
- add NEW template (which has a form to trigger post req create route)
- add CREATE route (creates then redirect to get INDEX)
- add CREATE template (dont think this was created?)

name="blog[title]" instead of name="image"/"url" so that items can be queried
from one object only (convenient/clean), the syntax is needed for middleware
body parser to properly parse it (explained a bit later in lecture 280)

# showtime
- add show route (leads to show template (GET))
- add show template
- add links to show page (leads to edit page (GET))
- style show template

    - <%- %> (unescaped raw output)
        #used here to render html, but need to handle sanitizing <script> tags to avoid malicious input
    - Date.toDateString() for human readable date
    - String.substring(indexStart, indexEnd)

# edit/update
- add edit route (GET)
    Blog.findByIdAndUpdate(req.params.id, req.body.blog, function(err, updatedBlog){}

- add edit form (same as update form)
- add update route (POST/PUT)
- add method-override
    - because no put/delete method support for html forms?
    # https://softwareengineering.stackexchange.com/questions/114156/why-are-there-are-no-put-and-delete-methods-on-html-forms
    - https://www.npmjs.com/package/method-override
    - method-override grabs defined "?_method" query string to override method
        - app.use(methodOverride("_method"));
        # <form action="/blogs/<%= blog._id %>?_method=put" method="post">

# destroy
- add destroy route
    Blog.findByIdAndRemove(req.params.id, callback)

- add edit and destroy links
    # hack to get destory link to submit to the form as an anchor
        <a onclick="this.parentElement.submit(), false">Delete</a>
    # css for pointer to change as it hovered over these anchorClicks
        .anchorClick {
            cursor: pointer;
        }
# final touches
- sanitize blog.body
    npm install express-sanitizer --save
    # expressSanitizer needs to be instantiated after `bodyParser`, and before anything that requires the sanitized input`
- style index


# alans commentse on this
'''
Just FYI, this whole form sync calls business is outdated.
its all AJAX now

Right now youre using Express to give you back HTML pages to load when you
submit a synchronous form call. Instead, AJAX submits asynchronously and gets
back a result, then the front end navigates to the page programmatically

Modern web pages are complicated.. it uses a hybrid of back end and front end
rendered HTML
'''



### data associations
- define associations
- discuss one:one, one:many, and many:many relationships

## embedding data - db blog_demo
    # embedding posts in user
    - define an entry (posts) of `type array of postSchema` in userSchema
                                        (this is the convention)
      const userSchema = new mongoose.Schema({
          email: String,
          name: String,
          posts: [postSchema]
      });
    - thus postSchema need to be created before userSchema

    User.findOne({name: "Hermione Granger"}, function(err, user){
        if(err){
            // console.log(err);
        } else {
            user.posts.push({
                title: "3 things i really hate.",
                content: "voldermort, voldermort and voldermort"
            });
            user.save(function(err, user){
                if(err){
                    console.log(err);
                } else {
                    console.log(user);
                }
            });
        }
    });
    # .save() is necesary to actually save to the db (even if you have updated
    #   the object locally in the script)

## referencing data (object references) - db blog_demo_2
    const userSchema = new mongoose.Schema({
        email: String,
        name: String,
        posts: [
            {
                type: mongoose.Schema.Types.ObjectId,
                ref: "Post"
            }
        ]
    });

    # create a bunch of posts (will be stored as ids in user)
    Post.create({
        title: "how to cook the best burger PART 3",
        content: "part 3's content"
    }, function(err, post){
        User.findOne({email: "bob@gmail.com"}, function(err, foundUser){
            if(err){
                console.log(err);
            } else {
                foundUser.posts.push(post);
                foundUser.save(function(err, data){
                    if(err){
                        console.log(err);
                    } else {
                        console.log("this is data: " + data);
                    }
                });
            }
        });
    });

    # find user and populate all posts with the actul post objects
    # feed in database name?: "Post" -> "posts"
    User.findOne({email: "bob@gmail.com"})
    .populate("posts")
    .exec(function(err, user){
        if(err){
            console.log(err);
        } else {
            console.log(user);
        }
    });

# Module.Exports (helps refactor)
- introduce module.exports (node.js)
- move our models into separate files

    # make post file
    const mongoose = require("mongoose");
    // POST - title, content
    const postSchema = new mongoose.Schema({
        title: String,
        content: String
    });
    module.exports = mongoose.model("Post", postSchema);

    # require in other file
    const Post = require("./models/post");



### yelpcamp: comments

## refactor mongoose code              ------ yelpcamp v3
- create module directory
- use module.exports
- require everything correctly

## add seed file (seeding the database)
- add seed.js file
- run the seed file everytime server starts

## add comment model
- display comment on campground show page

## comment new/create                  ------ yelpcamp v4
- nested routes
    # need to nest under camground id as comments exists under there
    NEW:    /campgrounds/:id/comments/new  #GET
    CREATE: /campgrounds/:id/comments      #POST
- add comment new/create routes
- add comment new form

## style show page                     ------ yelpcamp v5
# styling with bootstrap
- add side bar
- make comments look nice
    - .well (adds greyish background)
    - .caption ()



### authentication
# fyi colt source code: https://ide.c9.io/learnwithcolt/webdevbootcamp
# missing "auth from scratch" lectures, watch this after series for extra info:
  # https://www.youtube.com/watch?v=i7of02icPyQ

- order of library inclusion will be important (to not run into errors)
- tools:
    - Passport (http://www.passportjs.org/)
    - Passport Local (https://github.com/jaredhanson/passport-local)
    - Passport Local Mongoose (https://github.com/saintedlama/passport-local-mongoose)
- walk through auth flow
    - "sessions" allow us to have state in http requests
- discuss sessions
    - express-session

## auth code along part 1
- set up folder structure
- install packages
- add root route and template
- add secret route and template

## auth code along part 2
- create user model
    - plugged in passport mongoose in user model:
        const passportLocalMongoose = require("passport-local-mongoose");
        UserSchema.plugin(passportLocalMongoose);

- configure passport
    app.use(passport.initialize());
    app.use(passport.session());
    passport.serializeUser(User.serializeUser());       #encoding
    passport.deserializeUser(User.deserializeUser());   #decoding

    # User in this case is model with plugin passportLocalMongoose,
    # which already comes with serialize/deserialize, and we are just passing
    # it in to passport in app.js

- use and require express-session in one go:
    app.use(require("express-session")({
    secret: "all you can eat sushi",
    resave: false,
    saveUnitialized: false
    }));

## auth code along part 3
- add register route
- add register form

app.post("/register", function(req, res){
    # create new userobject, password is fed in separate to not
    #   be stored in db? (it will get turned into a hash, with "salt" to unhash?)

    # if all goes well we get a user object with the hash password in it
    User.register(new User({username: req.body.username}),
                  req.body.password, function(err, user){
        # if some error happens, return user to register page
        if(err){
            console.log(err);
            return res.render("register");
        }
        # no error, authenticate using chosen strategy (local in this case), and redirect to the page past authentication

        # this LOGS the user in
        passport.authenticate("local")(req, res, function(){
            res.redirect("/secret");
        });
    });
});

## auth code along part 4
- add login route
    login post:
        # login logic
        # middleware - runs before hitting the function associated with app.post("/login")
        # will check password
        app.post("/login", passport.authenticate("local", {
            successRedirect: "/secret",
            failureRedirect: "/login:"
        }), function(req, res){
        });

- add login form
- local strategy (why did we need this?)
    # creating a new local strategy using authenticate that is coming from passportLocalMongoose
    # (so we don't actually have to write the authenticate method either)
    # then tell password for the local strategy, use this method
    passport.use(new LocalStrategy(User.authenticate()));

## auth code along part 5
- add logout route
    # logout logic
    app.get("/logout", function(req, res){
        req.logout(); # exposed on req by passport.js ?
        res.redirect("/");
    })
- add isloggedin middleware
    # standard middleware definition pattern
    function isLoggedIn(req, res, next){
        # middleware for secret index(get) route
        if(req.isAuthenticated()){
            # knows to run the next function which is the callback for the route
            return next();
        }
        res.redirect("/login");
    }


# WATCH THIS ON AUTHENTICATION FOR IN-DEPTH AUTHENTICAION LEARNING
# ********* https://www.youtube.com/watch?v=i7of02icPyQ **********



### yelpcamp : adding authentication  ------ yelpcamp v6

# adding authentication1
- install packages needed for auth
- define user model

# adding authentication2
- configure passport
- add register route/template

# adding authentication3
- add login route/template

# adding authentication4
- add logout route
- prevent user from adding comment if not signed in
    - add isLoggedIn middleware to routes leading to the comment form
- add links to navbar

# adding authentication5
- show/hide auth links correctly
    - `req.user` is created by passport when you log in, which gives you
    `username`
    - included files also get access to variables passed into the file including it
      (in terms of a page including partials/header)
    - to pass in a variable to every route in one go, define and use a middleware
      http://expressjs.com/en/api.html#res.locals

        # views get to use currentUser now .. (beacuse res.locals?)
        # route files cant just call currentUser
        app.use(function(req, res, next){
            #pass in `currentUser`
            res.locals.currentUser = req.user;
            next();
        });

- confused why currentUser cant be used in routes/campgrounds.js, but can
  be used by partials/header.ejs
  - in route files with "res", can still be accessed via res.locals.varName,
    versus in rendered files you can just access it as varName



### yelpcamp: cleaning up           ------ yelpcamp v7

# refactor routes
- use express router to reorganize all routes
    - move all routes into routes/some_name.js
        - campgrounds, comments, index (more general: "/" and auth)
        - dry out routes names in routes files by supplying the common portion
          in app.js:
            app.use("/campgrounds/:id/comments", commentRoutes);

          - however you need to supply/preserve the parent route /campgrounds/:id
            req.params or else comments file will error, thus in comments file:

            router = express.Router({mergeParams: true})

# user / comments                   ------ yelpcamp v8
- associate users and comments
    - use objectId in comments model instead of just type string:
        const commentSchema = new mongoose.Schema({
            text: String,
            author: {
                id: {
                    type:  mongoose.Schema.Types.ObjectId,
                    ref: "User"
                },
                username: String
            }
        });

- save authors name to a comment automatically
    - sneak it in part of comment creation:
        newComment.author.id = req.user._id;
        newComment.author.username = req.user.username;
        newComment.save()


# user / campgrounds              ------ yelpcamp v9
- prevent unauthenticated user to create campground
    - isLoggedIn in campground create/post routes

- save username / id to newly created campground
    - update the same author object to campground model like done in comment




### yelpcamp: update and destroy

# editing/update campgrounds
- add method-override
- add edit route for campgrounds
- add link to edit page
- add upadate route

# deleting campgrounds
- add destroy route
- add delete button

# authorization
- user can only edit his/her campgrounds
- user can only delete his/her campgrounds

    -create a middelware

    function authorization(req, res, next){
        if(req.isAuthenticated()){
            Campground.findById(req.params.id, function(err, foundCampground){
                if(err){
                    res.redirect("back");
                } else {
                    if(foundCampground.author.id.equals(req.user._id)){
                        next();
                    } else {
                        res.redirect('back');
                    }
                }
            });
        } else {
            res.redirect("back");
        }
    }
    # foundCampground.author.id.equals(req.user._id)
    .equals() is an express method to help compare id object to id string,
    or else using === comparison between model.author.id and req.user._id would
    fail

    # res.redirect("back")
    manually typing in the url to go to an edit route does not give referer
        -christine yu

    # A back redirection redirects the request back to the referer,
    # defaulting to / when the referer is missing.
    keeps going back to '/'

- hide/show edit and delete buttons

    if(currentUser && campground.author.username === currentUser.username)

    if(currentUser && campground.author.id.equals(currentUser._id)

# editing comments
- add edit route for comments
- add edit button
- add update route

# deleting comments
- add destroy route / button

# authorization comments
- user can only edit their comments
- user can only delete their comments
- hide/show edit/delete buttons



### yelpcamp : ui improvements
# refactor middleware
    - put into middleware/index.js, and assign funtions to a middleware object
      to be exported

    - index.js is a special name in the sense that if you require a directory,
      it automatically requires the index file:
        thus require("express") = require("express/index")

# adding in flash text
    - install and configure connect-flash
        - install: npm install connect-flash --save
        - flash = require("...");
        - app.use(flash());
        - in middleware req.flash("key", "message") # BEFORE the redirect
        - in route locations:
            app.get('/flash', function(req, res){
            # Set a flash message by passing the key, followed by the value, to req.flash().
            req.flash('info', 'Flash is back!')
            res.redirect('/');
            });

            app.get('/', function(req, res){
            # Get an array of flash messages by passing the key to req.flash()
            res.render('index', { messages: req.flash('info') });
            });

            # also this?...
            return res.render("register", {"error": err.message});

    - add bootstrap alerts to header
        <div class="container">
            <% if(flashSuccess && flashSuccess.length > 0){ %>
                <div class="alert alert-success" role="alert">
                    <h4><%= flashSuccess %></h4>
                </div>
            <% } %>
            <% if(flashError && flashError.length > 0){ %>
                <div class="alert alert-danger" role="alert">
                    <h4><%= flashError %></h4>
                </div>
            <% } %>
        </div>

# extra notes on error handling
    if(err || !foundCampground){

    apparently you can change the id manually in the url and break the whole
    app (if changed id length is the same), so adding a foundCampground check
    in error catching resolves this

# landing page refactor
    # ian's stuff
    https://github.com/nax3t/background-slider

    - cutting out require header in the landing page (dont need navbar)
    - create separate landing.css stylesheet
    - source modernizer js (superfast tests that helps deliever tiered
        experience base on browser?..)
    - install/use `nodemon` if you want the ability to listen to file changes
    without restarting and run `node app.js` yourself

    - new css stuff..
        #landing-header {
          z-index: 1; # puts stuff in front of other items with lower z index
          position: relative; #default is static, needs to be relative to use z index
          text-align: center;
          padding-top: 40vh; # 40% view height? used to place header around middle
        }

    - using list items to be the changing background
      # https://developer.mozilla.org/en-US/docs/Web/CSS/position

        .slideshow {
          position: fixed; #doesn't move?
          width: 100%;
          height: 100%;
          top: 0;
          left: 0;
          z-index: 0;
          list-style: none; #remove bullet points
          margin: 0;
          padding: 0;
        }

        .slideshow li {
          width: 100%;
          height: 100%;
          position: absolute; # why absolute now? try changing it..
          top: 0;
          left: 0;
          background-size: cover;
          background-position: 50% 50%;
          background-repeat: no-repeat;
          opacity: 0;
          z-index: 0;
          animation: imageAnimation 50s linear infinite;
          # imageAnimation is the name of the animation, linear speed,
          # 50s repeat forever
        }


        .slideshow li:nth-child(1) {
          background-image: url(http://i.imgur.com/K3mPv14.jpg)
        }
        .slideshow li:nth-child(2) {
          background-image: url(http://i.imgur.com/SBEmFpv.jpg);
          animation-delay: 10s; #starts after 10s delay
        }
        .slideshow li:nth-child(3) {
          background-image: url(http://i.imgur.com/emvhOnb.jpg);
          animation-delay: 20s;
        }
        .slideshow li:nth-child(4) {
          background-image: url(http://i.imgur.com/2LSMCmJ.jpg);
          animation-delay: 30s;
        }
        .slideshow li:nth-child(5) {
          background-image: url(http://i.imgur.com/TVGe0Ef.jpg);
          animation-delay: 40s;
        }

        # The @keyframes CSS at-rule controls the intermediate steps in a CSS
        #　animation sequence by defining styles for keyframes
        #  https://developer.mozilla.org/en-US/docs/Web/CSS/%40keyframes

        # 100% = 50s
        # so 5 s to fade in
        # hold for 5 s

        # can't really tell what animation-timing-function is DOING..

    @keyframes imageAnimation {
      0% {
        opacity: 0;
        animation-timing-function: ease-in;
      }
      10% {
        opacity: 1;
        animation-timing-function: ease-out;
      }
      20% {
        opacity: 1
      }
      30% {
        opacity: 0
      }
    }

    # css animation intro:
    https://webdesign.tutsplus.com/tutorials/a-beginners-introduction-to-css-animation--cms-21068

# dynamic price feature
https://github.com/nax3t/dynamic-price
    - add 'price' as string in the campground model, but in new route/form,
      add price as input type of number (this allows input to be number but
        preserves the formatting?)


- fix $set problem #never end up addressing this one?

# TODO implement more refactoring
#  https://www.udemy.com/the-web-developer-bootcamp/learn/v4/questions/2078848
# TODO implement req.originalUrl
#  https://www.udemy.com/the-web-developer-bootcamp/learn/v4/questions/1886146



### Git and Github
# Ian's Intro to Git Course (https://www.udemy.com/intro-to-git/learn/v4/content)

- HEAD (current pointer, pointer in time)
- git --version # check if git is intalled on c9 (it is)
- git init
     - in directory level you want to track your repo
     - `rm -rf .git` if you want to remove it
- git add . # all files/dirs in current directory (working -> staging)
- git add -A # all files/dirs but also includes those in HIGHER directories
- git commit -m
- git log
- git revert --no-commit hashcode..head # reverting commit
- git branch -d branch_name # delete branch -D to HARD delete none merged
- git checkout -b branch_name

# three states
working         staging      .git directory(repository)
    |              |                     |
    |<-------check-out-the-project-------|
    |              |                     |
    |-stage-fixes->|                     |
    |              |-------commit------->|

working       : where files/changes/directories live
staging       : files/directories explicitly added
git repository: where all snapshots are stored

# ignoring files and folders
- .gitignore

# connecting c9 to github
- make a repo on github
- add c9 ssh key to github
- git remote add origin <url> # connect from c9 (sets up origin)
- got remote -v # check remote origin
- git push -u origin master


check directory size:
    du -sh *
    du --summary --human-readable *


### Deploying

# deploying simple app
commandline:
    - heroku login
    - make sure in a git repo (git init if you need to) / commit
    - heroku create
        git remote -v (to check for remote branches)
        gives you a link plus remote repo
        # https://tranquil-caverns-73549.herokuapp.com/
    - set up "start" script in package.json as "node app.js"
    - git push heroku master (push repo to heroku)
    - heroku logs (to view logs / error)

# deploying yelpcamp : basics
    - heroku run ls
        to run some command on the remote heroku repo

    - show info
        heroku info -s

# deploying yelpcamp : mongolab
    - sign up for mongolab  # https://mlab.com/

    - create db
        mongodb://<dbuser>:<dbpassword>@ds057204.mlab.com:57204/yelpcamp

        mongoose.connect("mongodb://localhost/yelp_camp_v12",
                         {useMongoClient: true});

        mongoose.connect("mongodb://sushi:sushi@ds057204.mlab.com:57204/yelpcamp",
                         {useMongoClient: true});

    - heroku domains : check domains
    - host www.davidsushi.com : check alias for "CNAME"?

# environment variables
    - export DATABASEURL =
        - mongoose.connect(process.env.DATABASEURL)

    - add var on heroku:
        - setting -> config variables -> add key/value
        or heroku config: set KEY=VALUE



### JavaScript: the tricky stuff (intermediate)

# keyword this - and four ways of looking at it
    - reserved JavaScript keyword
    - usually determined by the excecution context (how a function is called)
    - determined by 4 rules (global, object/implicit, explicit, new)

    - `global` (when this is not inside a declared object)
        - this would equal to `window`, which is the global object variables
            are attached to

        - when assigning this.var in a function, var is in turn a global variable
            attached to the window, this can be bad if you declare global variables
            by mistake

        - "use strict" phrase at the top of the code makes `this` undefined in
            functions instead of being the `window` object

    - `implicit`
        - the value of this will be the "closest" parent object
        - so if an object holds another object, the `this` within the second
            object will not be refering to the first object

    - `explicit` (use call, apply or bind to choose context of this?)
        # invoke immediately
            - Call (thisArg, a, b, c, d, ...)
            - Apply(thisArg, [a, b, c, d, ...])
        # returns function definition, can invoke later
            - Bind (thisArg, a, b, c, d, ...)

    # setTimeout() is a method of the window object
        - setTimeout doesnt run right away, so a call to this inside can end up
        getting the execution context of window instead of a parent object should
        you have call it from that object, in this case bind can solve the issue

        setTimeout(function().bind(this), delay)

    - `new` keyword (must be used with a function)
        - new keyword creates a new empty object out of thin air
        - in the function the keyword this refers to the new object created by new
        - an implicit `return this` is added to the end of the function

        -(1) adds a property __proto__ (which links the prototype on the constructor
              function to the empty object)
        -(2) creates a link (which we can access as __proto__) between the object
              created and the prototype property of the constructor function

              # prototype property is an object


# OOP (object oriented programming)
    - use constructor functions to reduce duplication in our code
    - use call and apply to refactor constructor functions
        function Dog()
        function Cat(){
            Dog.call(this, arguments)
        }

    # oop
    - construct object from classes (blueprint)
    - call objects created from classes `instances`

    # The arguments object is an Array-like object corresponding to the
    # arguments passed to a function.
    function blah(){
        console.log(arguments);
    }

    blah(1,2,3,4)
    Object {0: 2, 1: 3, 2: 4, length: 3…}

# OOP prototypes
    - understand prototype property(object)
    - describe and diagram relationshp between __proto__, prototype, constructor

        (object created by new + constructor can access the prototype
         property/object of the constructor via __proto__?)
        (but how/when did the constructor function get/create the prototype property?)


    Person(construc function) <--.constructor-- Person(.prototype object)
                              -- .prototype -->
                                                     ^            ^
                                                     | .__proto__ |
                                                     |            |
                                                    elie         colt

     # prototype chain
     when a method is not found in object A, JavaScript will go look for it in
     its __proto__ section, until theres no more __proto__ to look into, and
     return undefine

    - add methods and properties on the prototype object to write more efficient
        code

         Person.prototype.isIntructor = True;
         elie.isIntructor (True)
         cold.isIntructor (True)

    #example
    function Vehicle(make, model, year){
        this.make = make;
        this.model = model;
        this.year = year;
        this.isRunning = false;
    }

    Vehicle.prototype.turnOn = function(){
        this.isRunning = true;
    }

    Vehicle.prototype.turnOff = function(){
        this.isRunning = false;
    }

    Vehicle.prototype.honk = function(){
        if(this.isRunning){
            return "beep"
        }
    }

    - explain difference between adding methods and properties to the prototype
        versus the constructor function

        - method add to prototype should be expected to be used/shared by all
            objects that link to the prototype

# closures (the variable now lives in the closed space?)
- understand what closure is and what it is not
    - a closure is a function that makes use of variables defined in outer
        functions that have previously returned

    notes:
    - have to `return` the inner function for this to work
    - can either call inner function right away ()(), or store result from
        function in a variable, an call it later (similar to bind)
    - do NOT have to give inner fuction a name, could be anonymous

# example1
    function outer(){
        var data = "closures are ";
        return function inner(){
            var innerData = "awesome";
            return data + innerData;
        }
    }

    outer() - returns the function inner defintion
    outer()() - "closures are awesome" (using variables defined outside)

- use closure to emulate private variables
    - in above case `data` can no longer be called, but its running/used within
        the closure function

- list use cases for closures in real world


### END OF BOOTCAMP WHATTT   DEC.06.2017


# sushi image credit
<a href='https://www.freepik.com/free-vector/black-sushi-icons_761041.htm'>Designed by Freepik</a>
#




### ALAN'S EVENT LOOP LESSONS ###  Jan.16.2018
''' https://alanthai.github.io/event-loop-lessons/#introduction '''

- "JavaScript runs asynchronously through an event loop"

- "Assigning a new value to a variable that hasn't yet been declared with let/const/var will automatically declare it in the global scope. Never do this."

- "Despite being inside a method, normal function calls have a context of `window`. Don't forget!"
###


### MODERN JS CHEATSHEET ###
# https://github.com/mbeaudru/modern-js-cheatsheet#function-default-parameter-value

# =================================================================== #

### functional programming  ###
# Compute total grade sum for students with grades 10 or above by
# composing map, filter and reduce
students = [
  { 'name': "Nick", 'grade': 10 },
  { 'name': "John", 'grade': 15 },
  { 'name': "Julia", 'grade': 19 },
  { 'name': "Nathalie", 'grade': 9 }
]

grades        = map(lambda student: student['grade'], students)
grades_ten_up = filter(lambda grade: grade > 10, grades)
grades_total  = reduce(lambda x, y: x + y, grades_ten_up)

print grades_total

sum_grades_higher_than_ten = sum(
    grade for grade in (
        student['grade'] for student in students
    )
    if grade >10
)
print sum_grades_higher_than_ten



# PROMISES (https://scotch.io/tutorials/javascript-promises-for-dummies)
- 3 states: pending, resolved, rejected

# promise syntax look like this
new Promise(/* executor*/ function (resolve, reject) { ... } );

/* ES5 */
var isMomHappy = false;

# Promise
'''
lets asynchronous methods return values like synchronous methods: instead of
immediately returning the final value, the asynchronous method returns a promise
to supply the value at some point in the future.
'''
# promise create
var willIGetNewPhone = new Promise(
    function (resolve, reject) {
        if (isMomHappy) {
            var phone = {
                brand: 'Samsung',
                color: 'black'
            };
            resolve(phone); # fulfilled
        } else {
            var reason = new Error('mom is not happy');
            reject(reason); # reject
        }
    }
);

# promise consume
# call our promise

# The then() method returns a Promise. It takes up to two arguments: callback
# functions for the success and failure cases of the Promise.

var askMom = function () {
    willIGetNewPhone
        .then(function (fulfilled) {
            // yay, you got a new phone
            console.log(fulfilled);
         // output: { brand: 'Samsung', color: 'black' }
        })
        .catch(function (error) {
            # oops, mom don't buy it
            console.log(error.message);
         # output: 'mom is not happy'
        });
};
askMom();

# chain promise
# 2nd promise
var showOff = function (phone) {
    return new Promise(
        function (resolve, reject) {
            var message = 'Hey friend, I have a new ' +
                phone.color + ' ' + phone.brand + ' phone';

            resolve(message);
        }
    );
};

# reject is optional and example can be shortened using Promose.resolve()
# if reject is not run, the .catch() handler is just not attached to the promise

# 2nd promise
var showOff = function (phone) {
    var message = 'Hey friend, I have a new ' +
                phone.color + ' ' + phone.brand + ' phone';

    return Promise.resolve(message);
};

# chain (note promise is asynchronous, put it in .then() if you want it to
#    run after promise)
var askMom = function () {
    console.log('promises are async')
    willIGetNewPhone
    .then(showOff) # chain it here (first resolve return passes into here)
    .then(function (fulfilled) {
            console.log(fulfilled);
         # showOff fulfilled pass into here
         # output: 'Hey friend, I have a new black Samsung phone.'
        })
        .catch(function (error) {
            # oops, mom don't buy it
            console.log(error.message);
         # output: 'mom is not happy'
        });
    console.log('promises are async so this runs before "fufilled" message')
};


# ES6 ####################################################
/* ES6 */
const isMomHappy = true;

# Promise
const willIGetNewPhone = new Promise(
    (resolve, reject) => { // fat arrow
        if (isMomHappy) {
            const phone = {
                brand: 'Samsung',
                color: 'black'
            };
            resolve(phone);
        } else {
            const reason = new Error('mom is not happy');
            reject(reason);
        }
    }
);

# second promise
const showOff = function (phone) {
    const message = 'Hey friend, I have a new ' +
                phone.color + ' ' + phone.brand + ' phone';
    return Promise.resolve(message);
};

# call our promise
const askMom = function () {
    willIGetNewPhone
        .then(showOff)
        .then(fulfilled => console.log(fulfilled)) // fat arrow
        .catch(error => console.log(error.message)); // fat arrow
};

askMom();
# ES6 ####################################################

    let resultA, resultB, resultC;

    function addAsync (num1, num2, callback) {
        // use the famous jQuery getJSON callback API
        return $.getJSON('http://www.example.com', {
            num1: num1,
            num2: num2
        }, callback);
    }

    addAsync(1, 2, success => {
        // callback 1
        resultA = success; // you get result = 3 here

        addAsync(resultA, 3, success => {
            // callback 2
            resultB = success; // you get result = 6 here

            addAsync(resultB, 4, success => {
                // callback 3
                resultC = success; // you get result = 10 here

                console.log('total' + resultC);
                console.log(resultA, resultB, resultC);
            });
        });
    });
// rewrite above using promises
// add 1, 2, 3, 4
    const AddTwo = (num1, num2) => {
        return Promise.resolve(num1 + num2)
    }

    AddTwo(1, 2)
        .then(success => AddTwo(success, 3))
        .then(success => AddTwo(success, 4))
        .then(success => console.log(success))

# async and await
- prepend async whenever function returns a promise
    async function showOff(phone)
- prepend await whenever you need to call a promise
    let phone = await willIGetNewPhone; and let message = await showOff(phone);
- use try { ... } catch(error) { ... } to catch promise error, the rejected promise.


#### USING AYNC/AWAIT  ####
// add 1, 2, 3, 4 two at a time
// AddTwo = async(num1, num2) => {}
async function AddTwo(num1, num2){
    return Promise.resolve(num1 + num2);
}

async function AddNumbers(){
  try {
    let resultA = await AddTwo(1, 2);
    let resultB = await AddTwo(resultA, 3);
    let resultC = await AddTwo(resultB, 4);
    console.log(resultC);
  }
  catch(error){
    console.log(error.message);
  }
}

AddNumbers();

# - await operator can only be used in async function
# - await expressions needs to be wrapped in parentheses to call its resolved
#   value's methods and properties on the same line:
#   ex: const token = (await fetch('token_url')).json().token;
# - without using try/catch, uncaught exceptions will reject the promise:


# CLASS
- syntatic sugar for existing prototype based inheritance
- class declaration
    class Rectangle {
      constructor(height, width) {
        this.height = height;
        this.width = width;
      }
    }
- class expression
    // unnamed
    var Rectangle = class {
      constructor(height, width) {
        this.height = height;
        this.width = width;
      }
    };

    // named
    var Rectangle = class Rectangle {
      constructor(height, width) {
        this.height = height;
        this.width = width;
      }
    };
- super keyword must be used before the `this` keyword is used in constructor


# iterator patterns

#-------------PYTHON---------------------
class makeinterator(object):
  def __init__(self, some_list):
    self.next_index = 0
    self.some_list = some_list

  #makes class iterable
  def __iter__(self):
    return self

  def next(self):
    if self.next_index < len(self.some_list):
      next_num = self.some_list[self.next_index]
      self.next_index += 1
      return next_num
    else:
      raise StopIteration()

iterator = makeinterator([1,2])

print iterator.next()
print iterator.next()
print iterator.next()
#---------https://stackoverflow.com/questions/4020419/why-arent-python-nested-functions-called-closures/23558809#23558809
def make_iterator(n):
    next_list = [0]

    def next():
        next_index, = next_list
        if next_index >= len(n):
          raise StopIteration
        else:
          next_num = n[next_index]
          next_list[0] += 1
          return next_num

    return next

iter = make_iterator([1,2,3])

print(iter())
print(iter())
print(iter())
print(iter())

#-------------JavaScript-----------------
function makeIterator(n){
  nextIndex = 0;
  return {'next': function(){
    return nextIndex < n.length ?
      {'value': n[nextIndex++], 'done': false} :
      {'done': true};
    }
  };
}

iter = makeIterator([1,2]);

console.log(iter.next())
console.log(iter.next())
console.log(iter.next())
#----------------------------------------





# =================================================================== #

### Interview Prep on Tech Basics


### How the internet works for Developers p1 overview/frontend
# https://www.youtube.com/watch?v=e4S8zfLdLgQ&feature=youtu.be&list=PLoYCgNOIyGAB_8_iq1cL8MVeun7cB6eNc



### How the internet works for Developers p1 overview/frontend




### THE ADVANCED WEB DEVELOPER BOOTCAMP ###

# picking js/react route, but going to fit in time to look at AJAX w/Fetch
# + play flexbox frog



=======


Sharecode?
https://gist.github.com/

ChatRoom:

BootCamp
https://gitter.im/Colt/TheWebDeveloperBootcamp

CodeTalk
https://gitter.im/Colt/WDB-CodeTalk

JobTalk
https://gitter.im/Colt/WDB-Jobs


Syllabus:
1-18: front end
19-end: back end

course_slides:
https://drive.google.com/drive/folders/0B7qHXcyKO8LKWGdpcXQtM2liUjQ


requests
static/dynamic pages

HTML - structure (noun) -HyperText Markup Language
CSS - skin (adj) -Cascading Style Sheets
JavaScript - actions (verb)

sample: https://codepen.io/Colt/pen/WQQVvE
        https://codepen.io/anon/pen/GmYwrY (alan refactored)


sublime short cuts:
    html + tab gives html structure



###Intro to HTML:
- write properly structured html
- write closing/self-closing tags
- recreate simple website base on photo


elements: block/inline

lorem + tab (in html) to get random block text

generic containers:
    div - block
    span - inline

attributes:
    <a href=""></a>
    <img src="">



###Intermediate HTML:
-write valid html table
-write valid html forms using <form> <input> <select> <label>

html table
html form



###Intro to CSS:
-general rule of css
-correctly include css in html
-select elements by tag name, class and ID
-style elements with basic properties
-using chrome inspector tool to debug html/css

CSS samples:      http://www.csszengarden.com/
CSS color names:  http://colours.neilorangepeel.com/

General Rule：
selector{
    property: value;
    anotherProperty: value;
}

-can style via tag attributes
-can style via style tags (css sytax)
-ultimately style via link tag + separate .css file

Properties:
    Coloring:
        names (147 choices)
        color: red

        hexadecimal color:  0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
        color: #_ _ (R) _ _ (G) _ _ (B)

        rgb: each 0-255
        color: rgb(r, g, b)

        rgba: adds alpha ( 0.0-1.0 )
        color: rgba(r, g, b, a)

    Background:
        background: color
        background: url("http://blah.jpg")
        background-repeat: no-repeat;
        background-size: cover

    Border:
        border-color: purple;
        border-wide: 5px;
        border-style: solid;

        border: 5px solid purple;

    Text Decoration:
        text-decoration: line-through;

    float: left/right..etc (pulls element out of doc flow and floats it in a direction
        until it touches the border of the "containing box" or another floating element)

Selectors:
#https://code.tutsplus.com/tutorials/the-30-css-selectors-you-must-memorize--net-16048
#( but not really )
    #sharing attribute
    selector1, selector2 {
        attribute
    }


    element:
        element { }

    id:
        <p id="blah">
        "This attribute assigns a name to an element. This name must be unique in a document"
        #id_name { }

    class:
        <p class="blah">
        .class_name { }

        # class="A B" (multiple classes A and B)

    star: "applies to everything?"
        * { }

    combinators:
    descendent selector: "can be chained with other elements/selectors"
        li a { }  "any anchor tag inside an li"
        ul li .blah { }


    adjacent selector: "apply property to tags right after (not within) the parent"
        h1 + ul { blah }  "blah applied to ul(s) after all h1(s)"
    child selector:
        div:nth-of-type(3) > p {} "all p  inside third div"


    attribute selector: "apply property to tags with said attribute"
        a[href="http://blah"] { blah } "blah applied to all anchors with href blah"

        input[type="text"] { blah }

    nth of type:
        ul:nth-of-type(3) { blah } "apply property blah to every third ul"
        li:nth-of-type(3) { blah } "applies blah to the 'only third' li in each ol/ul (an ul with 6 li don't get blah applied twice "
        li:nth-of-type(3n) { blah } "same as above but repeated applies to every third"
        li:nth-of-type(even) { blah } "applies blah to EVERY 2nd li (multiple occurence in same ul/ol"

    pseudo class "specific state of class (hover, checked, visited"

    pseudo element "specific part of the element (first letter)"

Specificity:
    "selectors step over each other and the most specific one gets applied"

    "from least powerful to most powerful (in multiple power of 10s":

        #type selectors
            h1 + ul more powerful than h1
        #class , attribute, pseudo class selectors
            .hello{}
            input[type='text'] {}
            a:hover / input:checked
        #id selectors
            #hello



###Intermediate CSS:
- manipulate common font and text properties using css
- include external fonts using Google Fonts
- define and manipulate the four components of the Box Model

p {
    font-family: Arial;   # quotes needed if not one word
    font-size: 200px;
    font-size: 2.0em; #dynamic sizing (in this case double of parent)
               2.0rem; #rem is relative to html (root) font-size
    font-weight: bold; 100/200-800 (some fonts only);
    line-height: 2; #line spacing multiple base on font size
    text-align: right;center;
    text-decoration: underline;/line-through;
}


Google fonts: https://fonts.google.com/
-can find embedded links that can be used in your <head> (before your own css link <- optional or not?)
-dont select more font weights than you need as it adds page load time

HTML: <link href="https://fonts.googleapis.com/css?family=Lemonada" rel="stylesheet">
CSS : p { font-family: Lemonada; }


The Box Model:
- each element is represented as a rectangular box with four edges: margin edge, border edge, padding edge, content edge

p {
    border: 2px solid blue;
    padding: 10px;
    padding-left; 10px;
    margin: 50px;
    margin-top; 50px;
    margin: top right bottom left;
    margin: top/bottom right/left;   <-?
    margin top auto right auto; <- confirm what auto does
    0 dont need px
}



###Bootstrap:
- define bootstrap and explain why we use it (library)
- include bootstrap locally (download) and by using a CDN
- use common bootstrap components like navs and buttons
- build layout using bootstrap grid system

http://getbootstrap.com/

http://expo.getbootstrap.com/ #see how bootstrap is being used

bootstrap classes:
jumbotron (div - makes items within div a jumbotron)
container (div - place items with div in a margin-ed container)
form-group (div -makes grouped items closer to each other)
form-control (input -style and place inputs under labels)
form-inline (form - make items in form display in a line)

http://getbootstrap.com/components/#navbar

nav- navbar navbar-default
div - navbar-header
a - navbar-brand
div - collapse navbar-collapse
ul - nav navbar-nav
ul - nav navbar-nav navbar-right

the grid system: (12 column)
- has to be in a "container" class
- set size for parents: (example shows lg does not need to be set if you want it to be
    3 as well)
    <div> class="col-md-3 pink">col lg 3</div>
- four sizes: lg, md, sm, xs
- use class="row" for nesting grid
- use div-class="thumbnail" to constrain image size (this may not just work the way you want when you have various image sizes)
https://www.udemy.com/the-web-developer-bootcamp/learn/v4/t/lecture/6195846?start=0

    ~~ Alan on padding vs margin: ~~
    rule of thumb is "who is responsible", the parent or child
If you want spacing around your children, then padding on the parent...
if each element needs to space themselves, it is margin

- sometimes you will have to use inspector to find the selector thats having the effect on the style and use it to add the override you need (Specificity conflicts)

- bootstrap comes with usable icons:
    Glyphicons
- for more options theres also a bunch of icons available at fontsawesome:
    font awesome
    https://www.bootstrapcdn.com/fontawesome/
    http://fontawesome.io/icon/shower/



###Into to JS:
- evaluate js in chrome dev console
- 5 js primitives
- define use variables (var keyword)
- use built-in methods console.log, alert, prompt

variable declartion:
var var_name = var_value;

variable naming:
favors camelCase

undefined:
var defined but never given a value

null:
var defined explicitly as empty/nothingness


some built-in methods:
alert(value):
    an annoying print

console.log(value):
    print

prompt(value):
    prompt with "value", does return the entered value therefore can store
    as another var



###JS control flow:
- evaluate logical expressions
- 3-part conditional statements
- while/for loops
- translate between while/for loops

boolean:

== (5 == "5" is true)
=== (equal value and type, 5 === "5" is false)
!== (not equal value or equal type, 5 !== "5" is true)

type coercion for ==

99 == "99" true
99 === "999" false

null == undefined true
null === undefind false

logical operators:

&& AND, || OR, ! NOT

falsy values:
false, 0, "", null, undefind, NaN

conditionals:

if(condition) {doSomething}
else if(condition) {doSomething}
else {doSomething}

if() {
    doSomething;
} else {
    doSomething;
}

loops:
#DRY (dont repeat yourself)

while(condition) {doSomething}

for(var init; condition; step) {doSomething}



###JS basic functions:
-function declarations, function expressions
-console.log vs return
-define functions to take multiple arguments
-scope, higher functions

function functionName() {}
functionName();

in JS if an arg is not given it is just taken as an undefined, instead of giving
errors.


example with built-in methods:

#function declaration
function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}


#function expression (can later override what capitalize is)
var capitalize = function(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}


scope (the context that code is executed in)

'''thats what var is for without any qualifier, a variable declared in a
   function takes global scope. if you declare test as var test in the
   function, it wont overwrite the test outside '''

Higher Order functions
#take(as arg) or return a function

setInterval(function, millisecond) #returns a number

clearInterval(provide_returned_number_here_to_stop)

#anonymous function
function() {doSomething}



###JS arrays
- define and add data to arrays
- utilize built-in array methods
- console todo list

var arrayName = [blah, blah, blah];

#can assign directly to none existant index to grow array?
arrayName[4] = blah;

arrayName => [blah, blah, undefined x 1, blah]

var arrayName = [];
var arrayName = newArray(); #uncommon

array methods:
push/pop
shift/unshift
indexOf
slice

push: like python append but also returns length of array

unshift: add to front of array and return legnth of array
#array.insert(0, item)  item_array_ref.extend(array) in python?

shift: remove first item in array and return the removed item
# del array[0] in python?


var blah = "abcd"

blah.indexOf("a") => 0
blah.indexOf("e") => -1

#python blah.index("a")

slice: slice(start(gets included), end(not included))
[1,2,3].slice(1,2) => [2]  #python [1,2,3][1:2]

list.slice() #make a copy


#array iteration

array.forEach(someFunction)
# whether feeding a function or an anonymous function forEach by default expects
# arguments of ( item_per_items, index_item, items(array) )

# arr.forEach(function callback(currentValue, index, array) {
#     //your iterator
# }[, thisArg]);

# remove an item of item_index from array ONCE(?)
array.splice(index_to_delete, 1);
    # filter a very good option as well as it actually can return an array without the item (instead of an array of the removed items)
    # https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter

# for testing uniform in array consider array.every()
# https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every

#creating arrays
Array.from({ length: 5 }, (_, i) => i);
// => [0, 1, 2, 3, 4]

Array.from(Array(20).keys())
// => [0, 1, ..., 20]
#Array.from(Array(20).keys()).map(i => i + 1)   <= goes till 20


#arrow function syntax
() => {}
is equiv to
function() {}


###JS objects (key-value pairs)

#unlike arrays, objects have no order
    #don't need string keys like in python dictionary

#initialize object
1)
    var something = {};
2)
    var something = {
        key1: value,
        key2: value2
    };
3)
    var something = new Object();

#value retrieval
something["key1"] => value
something.key1 => value
    # dot notation limits: can't access key starting with number, with spacing

#js methods
#add method to object
#good for avoiding namspacing colliding
    #(same method names in diff object no collision)

a property inside an object hat is a function as a "method"

var something = {};

something.printStuff = function(stuff){
    console.log(stuff)
}

#`this` keyword

var something = {};
something.toPrint = [1,2,3];

#in here this refers to something, "this" will behave different in
#DIFFERENT CONTEXT
something.printStuff = function(){
    console.log(this.toPrint);
};



### DOM manipulation
- define what DOM is
- examples of sites using js to manipulate DOM
- understand SELECT, MANIPULATE workflow

'''
games, scrolling effects, dropdown menus, form validations
iteractivity, animations '''


http://patatap.com/


#document object model: interface between js and html+css

#warning console.dir(object) is a non-standard feature
console.dir(document) reveals the document object

#select and manipulate
#changing color to pink for h1
var h1 = document.querySelector("h1");
hi.style.color = "pink";

# five dom SELECTION methods
document.getElementByID()
# getElementsByClassName() returns an object (of objects) Nodelist?
# that's not quite an array (no forEach method..etc)
document.getElementsByClassName()
document.getElementsByTagName()

# querySelector methods pretty much replaces all getElement methods?
# querySelector() returns first element that matches css-style selector
document.querySelector("ul li")
document.querySelectorAll()

# MANIPULATION
- changing element style
- add/remove classes
- changing content of tag
- changing attributes (src, href)

# manipulate STYLE one at a time
var tag = document.getElementByID("blah"); #select

tag.style.color = "blue";                  #manipulate
tag.style.border = "10px solid red";
tag.style.fontSize = "70px";

# above is too repetitive (not DRY), need to have "separation of concerns"
# solution/alternative: define a new class then turn it on or off via js

# css
.some-class {
    color: blue;
    border: 10px solid red;
    fontSize: 79px;
}

# read-only property, not an array (probably really means don't support forEach)
tag.classList.add("some-class")
             .remove
             .toggle #also returns true/false

# manipulate text CONTENT
<p>This is <strong>blah</strong> boo</p>

var para = document.querySelector("p");
para.textContent #"This is blah boo"  <- doesn't show html tags
para.textContent = "boo boo boo"; # warning: this will not preserve origin html
                                  #          tags (such as strong)
para.innerHTML # "This is <strong>blah</strong> boo" <- shows html tags

para.innerHTML = "<strong> boo boo boo</strong>" # html will take effect, but
                                                 # no effect if assigned by
                                                 # textContent

# manipulate attributes
<a href="blah.com">Im blah link</a>
<img src="blah.png">

var link  = document.querySelector("a");
link.getAttribute("href"); #"blah.com"
link.setAttribute("href", "boo.com");

var img = document.querySelector("img");
img.setAttribute("src", "booo.png");



### advanced dom manipulation

# events
# clicking button / drag and drop / keypress / hovering over link

# add event listener to selected elements
element.addEventListener(type, functionToCall);

# another way to use `this`
# in this case `this` represents lis[i]
for(var i =  0; i < lis.length; i++){
    lis[i].addEventListener("click", function(){
        this.style.color = "pink";
        });
}

#https://developer.mozilla.org/en-US/docs/Web/Events
hover example: mouseover / mouseout

#irrelevant but interesting: wayback machine: https://web.archive.org/

use style.backgroundColor instead of style.background (doesnt work in firefox?)

# https://jsperf.com/concat-vs-plus-vs-join
string concatenation is fast in js? (not part of lecture)



''' FIXES to fix for number game  michael chen mchen
Object.keys(pScores).forEach(function(pKey, index){
Object.keys doesnt necessarily return the keys of your object in the order you wrote them
its the same thing as getting the keys of a python dictionary
a more unified way to do this is replace var pScores = {p1: 0, p2: 0}; with a more complex object that stores the scores as well as the p1count/p2count elements
like `var pState = {p1: {score: 0, element: p1Count}. p2: {score: 0, element: p2Count}}
var pState = {p1: {score: 0, element: p1Count}. p2: {score: 0, element: p2Count}}
var pState = {p1: {score: 0, element: p1Count}, p2: {score: 0, element: p2Count}}
and then just update this state
'''



### intro to jquery
-dom manipulation library
    - select/manipulate/create/animate elements
    - add event listener / effects
    - make http requests (ajax)
http://youmightnotneedjquery.com/

#previous reasons for using jquery:
    - fixes "broken" DOM api
    - brevity/clarity
    -cross-browser support
    -ajax
    -popular
#why not use jquery
    - DOM api no longer "broken"
    - doesn't do anything you can't do on your own
    - its an unnecessary dependency
    - performance
    - no longer popular

#adding jquery
- cdn: https://code.jquery.com/
- or local script text/JavaScript src it

check link by typing jQuery or $(a function) in console

# Ian note  In order to view the element you must access it via $('div')[0];
# https://stackoverflow.com/questions/13552432/show-elements-when-logging-jquery-object-in-chrome-dev-tools-console/13567689#13567689

#jquery selectors
$("selector") #returns ALL matching elements (a list even if one item)
$(".class")
$("#id")
$("li a")
    #first/last
    $().first(), $().last()

#manipulating style of all selected (don't need a new for loop)
$().css(property, value/object)
$("#blah").css("border", "2px solid red")

var styles = {
    color: "red",
    background: "pink",
    border: "2px solid purple"
}

$("#blah").css("border", styles)

$("#blah").css("border", {
    color: "red",
    background: "pink",
    border: "2px solid purple"
})

# jQuery methods

# val()
note: same discription as attr() but for getting/setting value
on input, select, textarea..etc

# text()
'Get the combined text contents of each element in the set of matched elements, including their descendants, or set the text contents of the matched elements.'
note: cant be used to set html

# attr()
'Get the value of an attribute for the first element in the set of matched elements or set one or more attributes for every matched element.'
note: similiar to .css() can feed in an object to set multiple attributes at once

# html()
'Get the HTML contents of the first element in the set of matched elements or set the HTML contents of every matched element.'

# addClass()
# removeClass()
# toggleClass()
    ~classList.methods() without the need of loops



### advanced jQuery

# events (most common)

# on() (MOST MOST COMMON?)
 - similar to addEventListener in which it lets you specify
the type of even to listen for

 - pretty much can use this for all events?

 - click() only adds listener for existing elements

 - on() will add listeners for all potential future elements(
    selector flag NEED TO BE specificed)
    .on( events [, selector ] [, data ], handler )
    # selector being a descendant of the element selected for on()


# click()
    # need to use jQuery version of "this" when "this" is desired
$().click(function {
    doSomething;
    $(this).css.(something)
    })

# keyPress()
the key pressed (shift + a ---> A)

    #getting the key pressed
    # event.which returns the key code http://keycode.info/
    keyPress(function(event/e){
        console.log(event.which)
        });


# jQuery effects
# https://api.jquery.com/category/effects/

# fadeOut
# http://api.jquery.com/fadeout/
# 'fast' and 'slow' can be supplied to indicate durations of 200 and 600 milliseconds, default being 400

.fadeOut( [duration ] [, complete ] )

note:
    - code does not wait for fadeOut to complete to run, therefore if
        that is the desired behaviour you should use a callback function
    for the [, complete] argument
    - fadeout turns diplay to none and does not remove html like
        $().remove() does


.fadeToggle() : similiar to classList.toggle for fadeOut/fadeIn

# slide: animates height, down to show up and up to go away
.slideDown / slideUp / slideToggle



### todo list  projects   jquery + html + css
- jquery: new methods, parent(), append(), creating elements,
    event delegation

- css: fontawesome, box shadow, transition , gradient


# event bubbling event.stopProgpation()
when you activate an event within parents/containers, the event can keep
firing up until it hits <html>, ex: a click event on body and a button in
body, clicking the button would trigger the button event, BUT also the body
event (body is treated as being clicked as well)

if this is undesirable the "event" object should be passed in the click
function and you can call event.stopProgpation()


# gradient
https://uigradients.com/



### patatap clone
- more exposure to third party libaries: paper.js, howler.js

# telling paperscript what id to look for(="canvas") for canvas
<script type="text/paperscript" canvas="canvas">


# l196 note:
'''
include paperscript code internally using script tag, if included as external
.js file it will break the app due to "cross origin resource sharing"

https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS
'''

# used paper.js for canvas operations, holwer.js for playing sounds



### intro to backend
- review internet basics, static vs dynamic sites, stacks/back end tech

www.udemy.com -> 23.234.47.175

# finding the right address
- query submitted to isp, within isp, the DNS takes the domain name and turns it into ip address

# going to that address
- request sent to desired ip via HTTP, finds fastest path to server with specified ip, requires hoping around servers

# udemy server responds
- requested server figures out what we are asking for, server builds right content (often pulling info from database), server responds with any combination of html, css and js

# static vs dynamic
- static sites always give you the same html, css, and js


# stacks
- see what stack companies use: https://stackshare.io/


# http requests
postman chrome app (good for debugging)

various http verbs (get (retrieval), post(add/submit usually via form) ..etc)

3 components of a response:
- body (content,pages source to be rendered into a web page?)
- header (meta data about the response: content type, date, time, status )
- status code(number that represents the response)


get request can still feed in some inputs via query string (?q=blah&haha=meh)



### the command line

# all cloud9 solutions for bootcamp
https://ide.c9.io/learnwithcolt/webdevbootcamp


https://www.davidbaumgold.com/tutorials/command-line/

ls, cd, mkdir, touch, rm , rm -rf
# most of these you can do multiple operations at once with a space between the inputs



### node js

what is node:
    what we use to run js on the server side


node "filename.js" # running a .js file


# what is npm: (latest movement is to use yarn?)
    - package manager for js

# why npm is good:
    - easy to use "npm install"

# packages we will be using:
    - mongoose, express, faker (exercise)

    - install package in the same directory as the file that is calling it (probably ways around this)

    - require() to include package :
      var faker = require('faker');



### server side frameworks

# what is a framework, how is it different from a library?
    - inversion of control, the framework calls you (vesus you call a library)
    - set ups where you fill in the predefined blank space

# what is express?
    - node web dev framework

# why are we using express?
    - light weight framework (vs rails is heavier)
        - more do it yourself (more blank space to fill vs less)


# routes
    - code that are responsible for receiving/lisetning requests, and deciding
      what to send back


# running the server
# node app.js -> preview running app
cloud 9 repo - https://ide.c9.io/lucidsushi/webdevbootcamp


# explain `--save` flag to install packages
'''`npm install <pkg> --save` afterwards to install a package and
save it as a dependency in the package.json file`'''

install multiple at once with `npm install <pkg1> <pkg2> --save

# explain package.json does
meta data which also includes what other packages are needed for it to run
(instead of including all the actual ingridients, give a list of ingridients)

# use `npm init` to create a new package.json

 '''
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

'''

# npm check package
npm list --depth=0 | grep package_name
npm ls package_name


# `*` route matcher will make everything
# route order matters, nothing else will get matched if * goes first
app.get("*", function(req, res) {
    res.send("You are a STAR!");
})

# routes containing route parameters/variables
# which makes the path not "hard coded"
prepend the param/var with a ":"

app.get("r/:something/blah/:boo");

can be queried via req.params => req.params.something // req.params.boo


# route order
further app.get() will not run when one is matched (kind of like elif statements)


# listen for requests (start server)
'''
// *** tell express to listen for requests (start server) ***
// need to use process.env.PORT (returns a number) for cloud9 instead of a direct number
// (os.environ['PORT'] in python)
app.listen(process.env.PORT, process.env.IP, function(){
    console.log("Server has started!!");
});
'''


### Intermediate express

# new tip: `c9 app.js` to open the file in editor on cloud 9
- express looks in "views" folder (not an arbitrary foldler name) for ejs

# use res.render() to render html from EJS file
feeding variable to ejs via objects:
    var name_in_current_scope = req.params.thing;
    res.render("love.ejs", {name_in_ejs: name_in_current_scope});

# what/why EJS https://www.npmjs.com/package/ejs
npm install ejs --save

# pass variable to EJS template
assign the special brackets + some var name =>  <%= varName %>
<h1>you fell in love with: <%= thingVar %></h1>
<%= thingVar.toUpperCase() %> #js methods support within brackets

code within brackets is treated as js code, then the return is passed to html

# ejs control flow
Escaped output with <%= %> (escape function configurable)
Control flow with <% %>

# styles and partials
- include public assets / serve public style sheet
  (images, CSS files, and JavaScript files)
    # https://expressjs.com/en/starter/static-files.html
    # tell express to serve the content of the "public" directory

    app.use(express.static("public"));
    app.use(express.static(__dirname + "/public")) #safer alternative

- configurate app to use ejs
    app.set("view engine", "ejs");# now no longer need to  put .ext for file
                                  # name inputs to res.render("file")
- use partial to dry up code
    -"partial" is a generic name
    - removes the need to repeatedly created the same html tag structure for each
      file in views
    - mkdir partials in 'views' folder
    - create header/footer.ejs files (the html from start to <body> being header,
                                      the html from </body> to </html> being footer)

    - for files in views add include statements at top and bottom:
        <% include partials/header %>
        <% include partials/footer %>

# post requests
- write post routes, test with postman
    app.post("/route", function)

- use a form to send post request
    <form action="/addfriend" method="post">

- use body parser to get form data
    'Parse incoming request bodies in a middleware (req.body?) before your'
    'handlers, available under the req.body property.'
    https://www.npmjs.com/package/body-parser
    npm install body-parser --save

    var bodyParser = require('body-parser');

    // This object will contain key-value pairs, where the value can be a string or
    //  array (when extended is false), or any type (when extended is true).
    app.use(bodyParser.urlencoded({ extended: true }));

    formData = req.body.name_of_input_in_form



### Working with APIs
# application programing interface
https://ifttt.com/
https://www.programmableweb.com/
- wep apis usually accessed through http requests
- make http request to api -> get some data back

# xml /json
xml - extended markup language - syntacticly similar to HTML, but does
not describe presentation like HTML does (ex: bold, strong)

json viewer chrome:
    https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh
    or http://jsonviewer.stack.hu/

# making api requests with node
- making requests in command-line using curl https://tldr.ostera.io/curl
- making requests in node using 'request': https://github.com/request/request

# %20 is how you encode "space" in an url

returned body could be just a string, therefore recast it to an objecting using:
    parseData = JSON.parse(body);

# using api key for request..
request vs request&apikey=thewdb



### Yelp Camp Basics
- add landing page
- add campground page that lists all campgrounds

    each campground has:
        -name
        -image

- create header/footer partials
- add bootstrap

- creating new campgrounds
    - setup new campground POST route
        share the same route name as get route to match REST convention/req
    - add in body parser
    - setup route to show form
    - add basic unstyle form

- style campground page
    - add better header/title
        - use double bootstrap containers as a trick to get the inner text to
          maintain some sort of padding when the page is shrunk in
    - make campgrounds display in a grid
        - <div class="row text-center" style="display: flex; flex-wrap: wrap;">
            - flex styling options used to make non-uniform images fit nicely

- style the navbar and formsomehow renaming a local folder doesnt break the git repo, any idea how this works?


1 /path/folder_name (master)

2 renames folder_name

3 /path/new_folder_name (master)
i want to rename the folder name, but not affect the repository in any way, like pull/push..etc
    - add navbar to all template

    - style new campground form
        - use bootstrap built-in <div class="form-group"> to put some vertical
        spacing between inputs



### databases

# intro to databases
- what is a database
    - collection of information/data
    - has an interface to interact with (db.dogs.find())
- sql (relational) vs. nosql (non-relational)
    - sql: tables, join tables, less flexible (new attributes need to be
        applied to all table entries)

    - nosql: dont need tables (doesnt mean its better than sql), more flexible

- what is mongodb (nosql)

- installing mongodb on c9
    - https://community.c9.io/t/setting-up-mongodb/1717

    - reparing mongo crash (if left running and timed out)
        cd ~
        ./mongod --repair

        # if still doesnt work
        cd ~/data
        rm mogod.lock
        cd
        ./mongod

-mongo commands
    # CRUD create/read/update/delete
    -mongod
        - starts the mongo daemon (process)
        # start it and leave it running in its own tab
    -mongo
        - launches mongodb shell
    -help
    -show dbs

    -use (sets current database or create it if it does not exist)
    -show collections (show collections in db)

    # below probably most important
    -insert
        - db.collection.insert(object)
            # unique "_id": ObjectId("") gets assigned by mongodb
    -find
        - db.collection.find() # shows the whole collection
        - db.collection.find(object) # shows entries matching object
    -update
        - db.collection.update(object_to_select, object_to_update)
            # this wipes out all other keys in the object
        - db.collection.update(object_to_select, {$set: object_to_update})
            # this will not wipe out keys not in original object that is not in
            # object to update
        - db.collection.update(object_to_select, {$set: object_to_update}, {
            multi: true})
            # additional extra flags exist to support certain operations, in
            # this case 'multi' needs to be set to true to actually update more
            # than one
    -remove
        - db.collection.remove({}) #removes everything
        - db.collection.remove(object_to_select) # removes all matching
        - db.collection.remove(object_to_select, {justOne: true}) # removes 1 match

# TODO (look into database migration)
# changing the db schema, like adding a property, and then looping through
# existing rows to update them all is called database migration.
# if you google mongodb db migration might help ya out


# intro to mongoose
    object data maper, object modeling tool (js layer on top of mongodb)

# some potential warnings
    ''' # 1
    Mongoose: mpromise (mongoose's default promise library) is deprecated,
    plug in your own promise library instead:
    http://mongoosejs.com/docs/promises.html
    '''
    # solution (after requiring mongoose):
    # replace mongoose's default promise library with js' native promise lib
    mongoose.Promise = global.Promise;


    ''' # 2
    `open()` is deprecated in mongoose >= 4.11.0, use `openUri()` instead,
    or set the `useMongoClient` option if using `connect()`
    or `createConnection()`
    '''
    # solution (instead of the regular mongoose.connect() syntax)
    mongoose.connect("mongodb://localhost/yelp_camp", {useMongoClient: true});

# using mongoose
    - elegant mongodb object modeling for node.js


    # creating schema
    const catSchema = new mongoose.Schema({
    name: String,
    age: Number,
    temperament: String
    });


    # compile to model (returns an object with useful methods)
    const Cat = mongoose.model("Cat", catSchema);
    "Cat" is the 'singular' version of the model, and collection 'Cats' gets
    created if it does not exist (always feed in singular, and it creates
        the plural somehow?)


    # add data to db
    # method 1
    const george = new Cat({
        name: "SushiCat",
        age: 2,
        temperament: "Tasty"
    });

    george.save(function(err, cat){
        if(err){
            console.log("something went wrong");
        } else {
            console.log("we just saved a cat to the db:");
            console.log(cat);
        }
    });

    # method 2
    Cat.create({
    name: "Angerrr",
    age: 10,
    temperament: "Pissed"
    }, function(err, cat){
        if(err){
            console.log(err);
        } else {
            console.log(cat);
        }
    });


    # retrieve all cats
    Cat.find({}, function(err, cats){
        if(err){
            console.log("oh no, ERROR");
            console.log(err);
        } else {
            console.log("all the cats....");
            console.log(cats);
        }
    });



### yelpcamp: data persistence
-install/configurate mongoose
-setup up campground model
-use camground model inside of our routes

'''random note
https://stackoverflow.com/questions/694102/declaring-multiple-variables-in-javascript
'''

# show page
- RESTful routes / rest table

name    url             verb    description                  mongoose
==========================================================================
INDEX   /dogs           GET     Display a list of dog        Dog.find()
NEW     /dogs/new       GET     show new form                N/A
CREATE  /dogs           POST    Add new dog to DB, redirect  Dog.create()
SHOW    /dogs/:id       GET     Shows info about one dog     Dog.findById()
EDIT    /dogs/:id/edit  GET     show edit form for one dog   Dog.findById()
UPDATE  /dogs/:id       PUT     update the dog, redirect     Dog.findByIdAndUpdate()
DESTROY /dogs/:id       DELETE  delete the dog, redirect     Dog.findByIdAndRemove()

# where in our examples update/destory use "post" by default, and method-override
# to correct verbs put/delete

# https://expressjs.com/en/guide/routing.html
# recall that /:parameter is convention for route parameters in express

- add description to campground model
- show db.collection.drop()
    returns true when successfully drops a collection (removes collection)
- add a show route/template



### RESTful routing
# Representational state transfer (REST)
REST - a mapping between HTTP routes and CRUD

# RESTful routes
https://gist.github.com/alexpchin/09939db6f81d654af06b

# blog index
- setup blog app
    ''' general app.js set up recap

    const express       = require("express"),
          mongoose      = require("mongoose"),
          bodyParser    = require("body-parser"),
          app           = express();

    // app config
    mongoose.connect("mongodb://localhost/yelp_camp", {useMongoClient: true});
    mongoose.Promise = global.Promise;
    app.use(bodyParser.urlencoded({extended: true}));
    app.use(express.static("public"));
    app.set("view engine", "ejs");


    app.listen(process.env.PORT, process.env.IP, function(){
        console.log("app.js running");
    });

    '''
- create the blog model
    - introduction to default value in mongoose schema:
        ex: "created: {type: Date, default: Date.now}," vs "created: Date,"
- add INDEX route and template

# basic layout
- add header/footer partials
- include semantic ui
    - similar to bootstrap + also has a bunch of icons (like fontawesome)
- add simple nav
    - served public asset app.css to enlarge icon (very specific selector to
        overcome libarys specificity)

# putting in the C in CRUD
- add NEW route
- add NEW template (which has a form to trigger post req create route)
- add CREATE route (creates then redirect to get INDEX)
- add CREATE template (dont think this was created?)

name="blog[title]" instead of name="image"/"url" so that items can be queried
from one object only (convenient/clean), the syntax is needed for middleware
body parser to properly parse it (explained a bit later in lecture 280)

# showtime
- add show route (leads to show template (GET))
- add show template
- add links to show page (leads to edit page (GET))
- style show template

    - <%- %> (unescaped raw output)
        #used here to render html, but need to handle sanitizing <script> tags to avoid malicious input
    - Date.toDateString() for human readable date
    - String.substring(indexStart, indexEnd)

# edit/update
- add edit route (GET)
    Blog.findByIdAndUpdate(req.params.id, req.body.blog, function(err, updatedBlog){}

- add edit form (same as update form)
- add update route (POST/PUT)
- add method-override
    - because no put/delete method support for html forms?
    # https://softwareengineering.stackexchange.com/questions/114156/why-are-there-are-no-put-and-delete-methods-on-html-forms
    - https://www.npmjs.com/package/method-override
    - method-override grabs defined "?_method" query string to override method
        - app.use(methodOverride("_method"));
        # <form action="/blogs/<%= blog._id %>?_method=put" method="post">

# destroy
- add destroy route
    Blog.findByIdAndRemove(req.params.id, callback)

- add edit and destroy links
    # hack to get destory link to submit to the form as an anchor
        <a onclick="this.parentElement.submit(), false">Delete</a>
    # css for pointer to change as it hovered over these anchorClicks
        .anchorClick {
            cursor: pointer;
        }
# final touches
- sanitize blog.body
    npm install express-sanitizer --save
    # expressSanitizer needs to be instantiated after `bodyParser`, and before anything that requires the sanitized input`
- style index


# alans commentse on this
'''
Just FYI, this whole form sync calls business is outdated.
its all AJAX now

Right now youre using Express to give you back HTML pages to load when you
submit a synchronous form call. Instead, AJAX submits asynchronously and gets
back a result, then the front end navigates to the page programmatically

Modern web pages are complicated.. it uses a hybrid of back end and front end
rendered HTML
'''



### data associations
- define associations
- discuss one:one, one:many, and many:many relationships

## embedding data - db blog_demo
    # embedding posts in user
    - define an entry (posts) of `type array of postSchema` in userSchema
                                        (this is the convention)
      const userSchema = new mongoose.Schema({
          email: String,
          name: String,
          posts: [postSchema]
      });
    - thus postSchema need to be created before userSchema

    User.findOne({name: "Hermione Granger"}, function(err, user){
        if(err){
            // console.log(err);
        } else {
            user.posts.push({
                title: "3 things i really hate.",
                content: "voldermort, voldermort and voldermort"
            });
            user.save(function(err, user){
                if(err){
                    console.log(err);
                } else {
                    console.log(user);
                }
            });
        }
    });
    # .save() is necesary to actually save to the db (even if you have updated
    #   the object locally in the script)

## referencing data (object references) - db blog_demo_2
    const userSchema = new mongoose.Schema({
        email: String,
        name: String,
        posts: [
            {
                type: mongoose.Schema.Types.ObjectId,
                ref: "Post"
            }
        ]
    });

    # create a bunch of posts (will be stored as ids in user)
    Post.create({
        title: "how to cook the best burger PART 3",
        content: "part 3's content"
    }, function(err, post){
        User.findOne({email: "bob@gmail.com"}, function(err, foundUser){
            if(err){
                console.log(err);
            } else {
                foundUser.posts.push(post);
                foundUser.save(function(err, data){
                    if(err){
                        console.log(err);
                    } else {
                        console.log("this is data: " + data);
                    }
                });
            }
        });
    });

    # find user and populate all posts with the actul post objects
    # feed in database name?: "Post" -> "posts"
    User.findOne({email: "bob@gmail.com"})
    .populate("posts")
    .exec(function(err, user){
        if(err){
            console.log(err);
        } else {
            console.log(user);
        }
    });

# Module.Exports (helps refactor)
- introduce module.exports (node.js)
- move our models into separate files

    # make post file
    const mongoose = require("mongoose");
    // POST - title, content
    const postSchema = new mongoose.Schema({
        title: String,
        content: String
    });
    module.exports = mongoose.model("Post", postSchema);

    # require in other file
    const Post = require("./models/post");



### yelpcamp: comments

## refactor mongoose code              ------ yelpcamp v3
- create module directory
- use module.exports
- require everything correctly

## add seed file (seeding the database)
- add seed.js file
- run the seed file everytime server starts

## add comment model
- display comment on campground show page

## comment new/create                  ------ yelpcamp v4
- nested routes
    # need to nest under camground id as comments exists under there
    NEW:    /campgrounds/:id/comments/new  #GET
    CREATE: /campgrounds/:id/comments      #POST
- add comment new/create routes
- add comment new form

## style show page                     ------ yelpcamp v5
# styling with bootstrap
- add side bar
- make comments look nice
    - .well (adds greyish background)
    - .caption ()



### authentication
# fyi colt source code: https://ide.c9.io/learnwithcolt/webdevbootcamp
# missing "auth from scratch" lectures, watch this after series for extra info:
  # https://www.youtube.com/watch?v=i7of02icPyQ

- order of library inclusion will be important (to not run into errors)
- tools:
    - Passport (http://www.passportjs.org/)
    - Passport Local (https://github.com/jaredhanson/passport-local)
    - Passport Local Mongoose (https://github.com/saintedlama/passport-local-mongoose)
- walk through auth flow
    - "sessions" allow us to have state in http requests
- discuss sessions
    - express-session

## auth code along part 1
- set up folder structure
- install packages
- add root route and template
- add secret route and template

## auth code along part 2
- create user model
    - plugged in passport mongoose in user model:
        const passportLocalMongoose = require("passport-local-mongoose");
        UserSchema.plugin(passportLocalMongoose);

- configure passport
    app.use(passport.initialize());
    app.use(passport.session());
    passport.serializeUser(User.serializeUser());       #encoding
    passport.deserializeUser(User.deserializeUser());   #decoding

    # User in this case is model with plugin passportLocalMongoose,
    # which already comes with serialize/deserialize, and we are just passing
    # it in to passport in app.js

- use and require express-session in one go:
    app.use(require("express-session")({
    secret: "all you can eat sushi",
    resave: false,
    saveUnitialized: false
    }));

## auth code along part 3
- add register route
- add register form

app.post("/register", function(req, res){
    # create new userobject, password is fed in separate to not
    #   be stored in db? (it will get turned into a hash, with "salt" to unhash?)

    # if all goes well we get a user object with the hash password in it
    User.register(new User({username: req.body.username}),
                  req.body.password, function(err, user){
        # if some error happens, return user to register page
        if(err){
            console.log(err);
            return res.render("register");
        }
        # no error, authenticate using chosen strategy (local in this case), and redirect to the page past authentication

        # this LOGS the user in
        passport.authenticate("local")(req, res, function(){
            res.redirect("/secret");
        });
    });
});

## auth code along part 4
- add login route
    login post:
        # login logic
        # middleware - runs before hitting the function associated with app.post("/login")
        # will check password
        app.post("/login", passport.authenticate("local", {
            successRedirect: "/secret",
            failureRedirect: "/login:"
        }), function(req, res){
        });

- add login form
- local strategy (why did we need this?)
    # creating a new local strategy using authenticate that is coming from passportLocalMongoose
    # (so we don't actually have to write the authenticate method either)
    # then tell password for the local strategy, use this method
    passport.use(new LocalStrategy(User.authenticate()));

## auth code along part 5
- add logout route
    # logout logic
    app.get("/logout", function(req, res){
        req.logout(); # exposed on req by passport.js ?
        res.redirect("/");
    })
- add isloggedin middleware
    # standard middleware definition pattern
    function isLoggedIn(req, res, next){
        # middleware for secret index(get) route
        if(req.isAuthenticated()){
            # knows to run the next function which is the callback for the route
            return next();
        }
        res.redirect("/login");
    }


# WATCH THIS ON AUTHENTICATION FOR IN-DEPTH AUTHENTICAION LEARNING
# ********* https://www.youtube.com/watch?v=i7of02icPyQ **********



### yelpcamp : adding authentication  ------ yelpcamp v6

# adding authentication1
- install packages needed for auth
- define user model

# adding authentication2
- configure passport
- add register route/template

# adding authentication3
- add login route/template

# adding authentication4
- add logout route
- prevent user from adding comment if not signed in
    - add isLoggedIn middleware to routes leading to the comment form
- add links to navbar

# adding authentication5
- show/hide auth links correctly
    - `req.user` is created by passport when you log in, which gives you
    `username`
    - included files also get access to variables passed into the file including it
      (in terms of a page including partials/header)
    - to pass in a variable to every route in one go, define and use a middleware
      http://expressjs.com/en/api.html#res.locals

        # views get to use currentUser now .. (beacuse res.locals?)
        # route files cant just call currentUser
        app.use(function(req, res, next){
            #pass in `currentUser`
            res.locals.currentUser = req.user;
            next();
        });

- confused why currentUser cant be used in routes/campgrounds.js, but can
  be used by partials/header.ejs
  - in route files with "res", can still be accessed via res.locals.varName,
    versus in rendered files you can just access it as varName



### yelpcamp: cleaning up           ------ yelpcamp v7

# refactor routes
- use express router to reorganize all routes
    - move all routes into routes/some_name.js
        - campgrounds, comments, index (more general: "/" and auth)
        - dry out routes names in routes files by supplying the common portion
          in app.js:
            app.use("/campgrounds/:id/comments", commentRoutes);

          - however you need to supply/preserve the parent route /campgrounds/:id
            req.params or else comments file will error, thus in comments file:

            router = express.Router({mergeParams: true})

# user / comments                   ------ yelpcamp v8
- associate users and comments
    - use objectId in comments model instead of just type string:
        const commentSchema = new mongoose.Schema({
            text: String,
            author: {
                id: {
                    type:  mongoose.Schema.Types.ObjectId,
                    ref: "User"
                },
                username: String
            }
        });

- save authors name to a comment automatically
    - sneak it in part of comment creation:
        newComment.author.id = req.user._id;
        newComment.author.username = req.user.username;
        newComment.save()


# user / campgrounds              ------ yelpcamp v9
- prevent unauthenticated user to create campground
    - isLoggedIn in campground create/post routes

- save username / id to newly created campground
    - update the same author object to campground model like done in comment




### yelpcamp: update and destroy

# editing/update campgrounds
- add method-override
- add edit route for campgrounds
- add link to edit page
- add upadate route

# deleting campgrounds
- add destroy route
- add delete button

# authorization
- user can only edit his/her campgrounds
- user can only delete his/her campgrounds

    -create a middelware

    function authorization(req, res, next){
        if(req.isAuthenticated()){
            Campground.findById(req.params.id, function(err, foundCampground){
                if(err){
                    res.redirect("back");
                } else {
                    if(foundCampground.author.id.equals(req.user._id)){
                        next();
                    } else {
                        res.redirect('back');
                    }
                }
            });
        } else {
            res.redirect("back");
        }
    }
    # foundCampground.author.id.equals(req.user._id)
    .equals() is an express method to help compare id object to id string,
    or else using === comparison between model.author.id and req.user._id would
    fail

    # res.redirect("back")
    manually typing in the url to go to an edit route does not give referer
        -christine yu

    # A back redirection redirects the request back to the referer,
    # defaulting to / when the referer is missing.
    keeps going back to '/'

- hide/show edit and delete buttons

    if(currentUser && campground.author.username === currentUser.username)

    if(currentUser && campground.author.id.equals(currentUser._id)

# editing comments
- add edit route for comments
- add edit button
- add update route

# deleting comments
- add destroy route / button

# authorization comments
- user can only edit their comments
- user can only delete their comments
- hide/show edit/delete buttons



### yelpcamp : ui improvements
# refactor middleware
    - put into middleware/index.js, and assign funtions to a middleware object
      to be exported

    - index.js is a special name in the sense that if you require a directory,
      it automatically requires the index file:
        thus require("express") = require("express/index")

# adding in flash text
    - install and configure connect-flash
        - install: npm install connect-flash --save
        - flash = require("...");
        - app.use(flash());
        - in middleware req.flash("key", "message") # BEFORE the redirect
        - in route locations:
            app.get('/flash', function(req, res){
            # Set a flash message by passing the key, followed by the value, to req.flash().
            req.flash('info', 'Flash is back!')
            res.redirect('/');
            });

            app.get('/', function(req, res){
            # Get an array of flash messages by passing the key to req.flash()
            res.render('index', { messages: req.flash('info') });
            });

            # also this?...
            return res.render("register", {"error": err.message});

    - add bootstrap alerts to header
        <div class="container">
            <% if(flashSuccess && flashSuccess.length > 0){ %>
                <div class="alert alert-success" role="alert">
                    <h4><%= flashSuccess %></h4>
                </div>
            <% } %>
            <% if(flashError && flashError.length > 0){ %>
                <div class="alert alert-danger" role="alert">
                    <h4><%= flashError %></h4>
                </div>
            <% } %>
        </div>

# extra notes on error handling
    if(err || !foundCampground){

    apparently you can change the id manually in the url and break the whole
    app (if changed id length is the same), so adding a foundCampground check
    in error catching resolves this

# landing page refactor
    # ian's stuff
    https://github.com/nax3t/background-slider

    - cutting out require header in the landing page (dont need navbar)
    - create separate landing.css stylesheet
    - source modernizer js (superfast tests that helps deliever tiered
        experience base on browser?..)
    - install/use `nodemon` if you want the ability to listen to file changes
    without restarting and run `node app.js` yourself

    - new css stuff..
        #landing-header {
          z-index: 1; # puts stuff in front of other items with lower z index
          position: relative; #default is static, needs to be relative to use z index
          text-align: center;
          padding-top: 40vh; # 40% view height? used to place header around middle
        }

    - using list items to be the changing background
      # https://developer.mozilla.org/en-US/docs/Web/CSS/position

        .slideshow {
          position: fixed; #doesn't move?
          width: 100%;
          height: 100%;
          top: 0;
          left: 0;
          z-index: 0;
          list-style: none; #remove bullet points
          margin: 0;
          padding: 0;
        }

        .slideshow li {
          width: 100%;
          height: 100%;
          position: absolute; # why absolute now? try changing it..
          top: 0;
          left: 0;
          background-size: cover;
          background-position: 50% 50%;
          background-repeat: no-repeat;
          opacity: 0;
          z-index: 0;
          animation: imageAnimation 50s linear infinite;
          # imageAnimation is the name of the animation, linear speed,
          # 50s repeat forever
        }


        .slideshow li:nth-child(1) {
          background-image: url(http://i.imgur.com/K3mPv14.jpg)
        }
        .slideshow li:nth-child(2) {
          background-image: url(http://i.imgur.com/SBEmFpv.jpg);
          animation-delay: 10s; #starts after 10s delay
        }
        .slideshow li:nth-child(3) {
          background-image: url(http://i.imgur.com/emvhOnb.jpg);
          animation-delay: 20s;
        }
        .slideshow li:nth-child(4) {
          background-image: url(http://i.imgur.com/2LSMCmJ.jpg);
          animation-delay: 30s;
        }
        .slideshow li:nth-child(5) {
          background-image: url(http://i.imgur.com/TVGe0Ef.jpg);
          animation-delay: 40s;
        }

        # The @keyframes CSS at-rule controls the intermediate steps in a CSS
        #　animation sequence by defining styles for keyframes
        #  https://developer.mozilla.org/en-US/docs/Web/CSS/%40keyframes

        # 100% = 50s
        # so 5 s to fade in
        # hold for 5 s

        # can't really tell what animation-timing-function is DOING..

    @keyframes imageAnimation {
      0% {
        opacity: 0;
        animation-timing-function: ease-in;
      }
      10% {
        opacity: 1;
        animation-timing-function: ease-out;
      }
      20% {
        opacity: 1
      }
      30% {
        opacity: 0
      }
    }

    # css animation intro:
    https://webdesign.tutsplus.com/tutorials/a-beginners-introduction-to-css-animation--cms-21068

# dynamic price feature
https://github.com/nax3t/dynamic-price
    - add 'price' as string in the campground model, but in new route/form,
      add price as input type of number (this allows input to be number but
        preserves the formatting?)


- fix $set problem #never end up addressing this one?

# TODO implement more refactoring
#  https://www.udemy.com/the-web-developer-bootcamp/learn/v4/questions/2078848
# TODO implement req.originalUrl
#  https://www.udemy.com/the-web-developer-bootcamp/learn/v4/questions/1886146



### Git and Github
# Ian's Intro to Git Course (https://www.udemy.com/intro-to-git/learn/v4/content)

- HEAD (current pointer, pointer in time)
- git --version # check if git is intalled on c9 (it is)
- git init
     - in directory level you want to track your repo
     - `rm -rf .git` if you want to remove it
- git add . # all files/dirs in current directory (working -> staging)
- git add -A # all files/dirs but also includes those in HIGHER directories
- git commit -m
- git log
- git revert --no-commit hashcode..head # reverting commit
- git branch -d branch_name # delete branch -D to HARD delete none merged
- git checkout -b branch_name

# three states
working         staging      .git directory(repository)
    |              |                     |
    |<-------check-out-the-project-------|
    |              |                     |
    |-stage-fixes->|                     |
    |              |-------commit------->|

working       : where files/changes/directories live
staging       : files/directories explicitly added
git repository: where all snapshots are stored

# ignoring files and folders
- .gitignore

# connecting c9 to github
- make a repo on github
- add c9 ssh key to github
- git remote add origin <url> # connect from c9 (sets up origin)
- got remote -v # check remote origin
- git push -u origin master


check directory size:
    du -sh *
    du --summary --human-readable *


### Deploying

# deploying simple app
commandline:
    - heroku login
    - make sure in a git repo (git init if you need to) / commit
    - heroku create
        git remote -v (to check for remote branches)
        gives you a link plus remote repo
        # https://tranquil-caverns-73549.herokuapp.com/
    - set up "start" script in package.json as "node app.js"
    - git push heroku master (push repo to heroku)
    - heroku logs (to view logs / error)

# deploying yelpcamp : basics
    - heroku run ls
        to run some command on the remote heroku repo

    - show info
        heroku info -s

# deploying yelpcamp : mongolab
    - sign up for mongolab  # https://mlab.com/

    - create db
        mongodb://<dbuser>:<dbpassword>@ds057204.mlab.com:57204/yelpcamp

        mongoose.connect("mongodb://localhost/yelp_camp_v12",
                         {useMongoClient: true});

        mongoose.connect("mongodb://sushi:sushi@ds057204.mlab.com:57204/yelpcamp",
                         {useMongoClient: true});

    - heroku domains : check domains
    - host www.davidsushi.com : check alias for "CNAME"?

# environment variables
    - export DATABASEURL =
        - mongoose.connect(process.env.DATABASEURL)

    - add var on heroku:
        - setting -> config variables -> add key/value
        or heroku config: set KEY=VALUE



### JavaScript: the tricky stuff (intermediate)

# keyword this - and four ways of looking at it
    - reserved JavaScript keyword
    - usually determined by the excecution context (how a function is called)
    - determined by 4 rules (global, object/implicit, explicit, new)

    - `global` (when this is not inside a declared object)
        - this would equal to `window`, which is the global object variables
            are attached to

        - when assigning this.var in a function, var is in turn a global variable
            attached to the window, this can be bad if you declare global variables
            by mistake

        - "use strict" phrase at the top of the code makes `this` undefined in
            functions instead of being the `window` object

    - `implicit`
        - the value of this will be the "closest" parent object
        - so if an object holds another object, the `this` within the second
            object will not be refering to the first object

    - `explicit` (use call, apply or bind to choose context of this?)
        # invoke immediately
            - Call (thisArg, a, b, c, d, ...)
            - Apply(thisArg, [a, b, c, d, ...])
        # returns function definition, can invoke later
            - Bind (thisArg, a, b, c, d, ...)

    # setTimeout() is a method of the window object
        - setTimeout doesnt run right away, so a call to this inside can end up
        getting the execution context of window instead of a parent object should
        you have call it from that object, in this case bind can solve the issue

        setTimeout(function().bind(this), delay)

    - `new` keyword (must be used with a function)
        - new keyword creates a new empty object out of thin air
        - in the function the keyword this refers to the new object created by new
        - an implicit `return this` is added to the end of the function

        -(1) adds a property __proto__ (which links the prototype on the constructor
              function to the empty object)
        -(2) creates a link (which we can access as __proto__) between the object
              created and the prototype property of the constructor function

              # prototype property is an object


# OOP (object oriented programming)
    - use constructor functions to reduce duplication in our code
    - use call and apply to refactor constructor functions
        function Dog()
        function Cat(){
            Dog.call(this, arguments)
        }

    # oop
    - construct object from classes (blueprint)
    - call objects created from classes `instances`

    # The arguments object is an Array-like object corresponding to the
    # arguments passed to a function.
    function blah(){
        console.log(arguments);
    }

    blah(1,2,3,4)
    Object {0: 2, 1: 3, 2: 4, length: 3…}

# OOP prototypes
    - understand prototype property(object)
    - describe and diagram relationshp between __proto__, prototype, constructor

        (object created by new + constructor can access the prototype
         property/object of the constructor via __proto__?)
        (but how/when did the constructor function get/create the prototype property?)


    Person(construc function) <--.constructor-- Person(.prototype object)
                              -- .prototype -->
                                                     ^            ^
                                                     | .__proto__ |
                                                     |            |
                                                    elie         colt

     # prototype chain
     when a method is not found in object A, JavaScript will go look for it in
     its __proto__ section, until theres no more __proto__ to look into, and
     return undefine

    - add methods and properties on the prototype object to write more efficient
        code

         Person.prototype.isIntructor = True;
         elie.isIntructor (True)
         cold.isIntructor (True)

    #example
    function Vehicle(make, model, year){
        this.make = make;
        this.model = model;
        this.year = year;
        this.isRunning = false;
    }

    Vehicle.prototype.turnOn = function(){
        this.isRunning = true;
    }

    Vehicle.prototype.turnOff = function(){
        this.isRunning = false;
    }

    Vehicle.prototype.honk = function(){
        if(this.isRunning){
            return "beep"
        }
    }

    - explain difference between adding methods and properties to the prototype
        versus the constructor function

        - method add to prototype should be expected to be used/shared by all
            objects that link to the prototype

# closures (the variable now lives in the closed space?)
- understand what closure is and what it is not
    - a closure is a function that makes use of variables defined in outer
        functions that have previously returned

    notes:
    - have to `return` the inner function for this to work
    - can either call inner function right away ()(), or store result from
        function in a variable, an call it later (similar to bind)
    - do NOT have to give inner fuction a name, could be anonymous

# example1
    function outer(){
        var data = "closures are ";
        return function inner(){
            var innerData = "awesome";
            return data + innerData;
        }
    }

    outer() - returns the function inner defintion
    outer()() - "closures are awesome" (using variables defined outside)

- use closure to emulate private variables
    - in above case `data` can no longer be called, but its running/used within
        the closure function

- list use cases for closures in real world


### END OF BOOTCAMP WHATTT   DEC.06.2017


# sushi image credit
<a href='https://www.freepik.com/free-vector/black-sushi-icons_761041.htm'>Designed by Freepik</a>
#




### ALAN'S EVENT LOOP LESSONS ###  Jan.16.2018
''' https://alanthai.github.io/event-loop-lessons/#introduction '''

- "JavaScript runs asynchronously through an event loop"

- "Assigning a new value to a variable that hasn't yet been declared with let/const/var will automatically declare it in the global scope. Never do this."

- "Despite being inside a method, normal function calls have a context of `window`. Don't forget!"
###


### MODERN JS CHEATSHEET ###
# https://github.com/mbeaudru/modern-js-cheatsheet#function-default-parameter-value

# =================================================================== #

### functional programming  ###
# Compute total grade sum for students with grades 10 or above by
# composing map, filter and reduce
students = [
  { 'name': "Nick", 'grade': 10 },
  { 'name': "John", 'grade': 15 },
  { 'name': "Julia", 'grade': 19 },
  { 'name': "Nathalie", 'grade': 9 }
]

grades        = map(lambda student: student['grade'], students)
grades_ten_up = filter(lambda grade: grade > 10, grades)
grades_total  = reduce(lambda x, y: x + y, grades_ten_up)

print grades_total

sum_grades_higher_than_ten = sum(
    grade for grade in (
        student['grade'] for student in students
    )
    if grade >10
)
print sum_grades_higher_than_ten



# PROMISES (https://scotch.io/tutorials/javascript-promises-for-dummies)
- 3 states: pending, resolved, rejected

# promise syntax look like this
new Promise(/* executor*/ function (resolve, reject) { ... } );

/* ES5 */
var isMomHappy = false;

# Promise
'''
lets asynchronous methods return values like synchronous methods: instead of
immediately returning the final value, the asynchronous method returns a promise
to supply the value at some point in the future.
'''
# promise create
var willIGetNewPhone = new Promise(
    function (resolve, reject) {
        if (isMomHappy) {
            var phone = {
                brand: 'Samsung',
                color: 'black'
            };
            resolve(phone); # fulfilled
        } else {
            var reason = new Error('mom is not happy');
            reject(reason); # reject
        }
    }
);

# promise consume
# call our promise

# The then() method returns a Promise. It takes up to two arguments: callback
# functions for the success and failure cases of the Promise.

var askMom = function () {
    willIGetNewPhone
        .then(function (fulfilled) {
            // yay, you got a new phone
            console.log(fulfilled);
         // output: { brand: 'Samsung', color: 'black' }
        })
        .catch(function (error) {
            # oops, mom don't buy it
            console.log(error.message);
         # output: 'mom is not happy'
        });
};
askMom();

# chain promise
# 2nd promise
var showOff = function (phone) {
    return new Promise(
        function (resolve, reject) {
            var message = 'Hey friend, I have a new ' +
                phone.color + ' ' + phone.brand + ' phone';

            resolve(message);
        }
    );
};

# reject is optional and example can be shortened using Promose.resolve()
# if reject is not run, the .catch() handler is just not attached to the promise

# 2nd promise
var showOff = function (phone) {
    var message = 'Hey friend, I have a new ' +
                phone.color + ' ' + phone.brand + ' phone';

    return Promise.resolve(message);
};

# chain (note promise is asynchronous, put it in .then() if you want it to
#    run after promise)
var askMom = function () {
    console.log('promises are async')
    willIGetNewPhone
    .then(showOff) # chain it here (first resolve return passes into here)
    .then(function (fulfilled) {
            console.log(fulfilled);
         # showOff fulfilled pass into here
         # output: 'Hey friend, I have a new black Samsung phone.'
        })
        .catch(function (error) {
            # oops, mom don't buy it
            console.log(error.message);
         # output: 'mom is not happy'
        });
    console.log('promises are async so this runs before "fufilled" message')
};


# ES6 ####################################################
/* ES6 */
const isMomHappy = true;

# Promise
const willIGetNewPhone = new Promise(
    (resolve, reject) => { // fat arrow
        if (isMomHappy) {
            const phone = {
                brand: 'Samsung',
                color: 'black'
            };
            resolve(phone);
        } else {
            const reason = new Error('mom is not happy');
            reject(reason);
        }
    }
);

# second promise
const showOff = function (phone) {
    const message = 'Hey friend, I have a new ' +
                phone.color + ' ' + phone.brand + ' phone';
    return Promise.resolve(message);
};

# call our promise
const askMom = function () {
    willIGetNewPhone
        .then(showOff)
        .then(fulfilled => console.log(fulfilled)) // fat arrow
        .catch(error => console.log(error.message)); // fat arrow
};

askMom();
# ES6 ####################################################

    let resultA, resultB, resultC;

    function addAsync (num1, num2, callback) {
        // use the famous jQuery getJSON callback API
        return $.getJSON('http://www.example.com', {
            num1: num1,
            num2: num2
        }, callback);
    }

    addAsync(1, 2, success => {
        // callback 1
        resultA = success; // you get result = 3 here

        addAsync(resultA, 3, success => {
            // callback 2
            resultB = success; // you get result = 6 here

            addAsync(resultB, 4, success => {
                // callback 3
                resultC = success; // you get result = 10 here

                console.log('total' + resultC);
                console.log(resultA, resultB, resultC);
            });
        });
    });
// rewrite above using promises
// add 1, 2, 3, 4
    const AddTwo = (num1, num2) => {
        return Promise.resolve(num1 + num2)
    }

    AddTwo(1, 2)
        .then(success => AddTwo(success, 3))
        .then(success => AddTwo(success, 4))
        .then(success => console.log(success))

# async and await
- prepend async whenever function returns a promise
    async function showOff(phone)
- prepend await whenever you need to call a promise
    let phone = await willIGetNewPhone; and let message = await showOff(phone);
- use try { ... } catch(error) { ... } to catch promise error, the rejected promise.


#### USING AYNC/AWAIT  ####
// add 1, 2, 3, 4 two at a time
// AddTwo = async(num1, num2) => {}
async function AddTwo(num1, num2){
    return Promise.resolve(num1 + num2);
}

async function AddNumbers(){
  try {
    let resultA = await AddTwo(1, 2);
    let resultB = await AddTwo(resultA, 3);
    let resultC = await AddTwo(resultB, 4);
    console.log(resultC);
  }
  catch(error){
    console.log(error.message);
  }
}

AddNumbers();

# - await operator can only be used in async function
# - await expressions needs to be wrapped in parentheses to call its resolved
#   value's methods and properties on the same line:
#   ex: const token = (await fetch('token_url')).json().token;


# CLASS
- syntatic sugar for existing prototype based inheritance
- class declaration
    class Rectangle {
      constructor(height, width) {
        this.height = height;
        this.width = width;
      }
    }
- class expression
    // unnamed
    var Rectangle = class {
      constructor(height, width) {
        this.height = height;
        this.width = width;
      }
    };

    // named
    var Rectangle = class Rectangle {
      constructor(height, width) {
        this.height = height;
        this.width = width;
      }
    };
- super keyword must be used before the `this` keyword is used in constructor





# =================================================================== #

### Interview Prep on Tech Basics


### How the internet works for Developers p1 overview/frontend
# https://www.youtube.com/watch?v=e4S8zfLdLgQ&feature=youtu.be&list=PLoYCgNOIyGAB_8_iq1cL8MVeun7cB6eNc



### How the internet works for Developers p1 overview/frontend




### THE ADVANCED WEB DEVELOPER BOOTCAMP ###

# picking js/react route, but going to fit in time to look at AJAX w/Fetch
# + play flexbox frog



>>>>>>> b744acc7b64d47d0d0d4969209a8d90d2499d351:dev_notes.py
