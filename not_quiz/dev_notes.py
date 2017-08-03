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
	element:
		element{}

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
		li a { }
		ul li .blah { } "any anchor tag inside an li"


	adjacent selector: "apply property to tags right after (not within) the parent"
		h1 + ul { blah }  "blah applied to ul(s) after all h1(s)"
	child selector:
		div:nth-of-type(3) > p {} "all p  inside third div"


	attribute selector: "apply property to tags with said attribute"
		a[href="http://blahz"] { blah } "blah applied to all anchors with href blahz"

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