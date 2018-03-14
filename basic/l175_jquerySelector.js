// select al ldivs and give purple bg
$("div").css("background", "purple");

//select elements with class highlight and change width
$(".highlight").css("width", "200px");

//select id "third" and give orange border
$("#third").css("border", "3px solid orange");

// select first div and change text color to pink

//$("div:nth-of-type(1)").css("color", "pink");
//$("div:first-of-type").css("color", "pink");

//jquery built-in , but slower than css built-in first-of-type
$("div:first").css("color", "pink");