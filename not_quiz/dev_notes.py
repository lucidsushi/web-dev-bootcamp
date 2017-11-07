You can share your code with us in a Q&A thread by using the {...} code block button (first write your code, select it, then press the button



- Introduce yourself on the discussion boards and chatrooms
- Ask questions
- Help answer other students’ questions
- Post your own solutions to projects and exercises
- Share links to helpful articles and tutorials
- Share your own blog posts (shoutout to Jamal Yusef for some great content)
- Share your personal projects
- Share feedback on individual lessons, sections, and the course in general


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

the grid system:
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
// =. [0, 1, ..., 20]
#Array.from(Array(20).keys()).map(i => i + 1)   <= goes till 20


#array function syntax
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

    - install packcage in the same directory as the file that is calling it (probably ways around this)

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
- include public assets
    #tell express to serve the content of the "public" directory
    app.use(express.static("public"));

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

- style the navbar and form
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
        - db.collection.remove(object_to_select) # removes all matching
        - db.collection.remove(object_to_select, {justOne: true}) # removes 1 match


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

# mongoose
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


    # add cat to db
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



# yelpcamp: data persistence











