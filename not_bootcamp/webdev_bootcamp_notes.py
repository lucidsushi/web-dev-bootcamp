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
elements: block/inline

lorem + tab (in html) to get random block text

generic containers:
	div - block
	span - inline

attributes:
	<a href=""></a>
	<img src="">

###Intermediate HTML:
html table
html form

###Intro to CSS:
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

Selectors:
	element:
		element{}

	id:
		<p id="blah">
		"This attribute assigns a name to an element. This name must be unique in a document"
		#id_name { }

	class:
		<p class="blah">
		.class_name { }

	star:
		* { }

	descendent selection: "can be chained with other elements/selectors"
		li a { }
		"any anchor tag inside an li"