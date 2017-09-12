// event bubbling check
$("body").on("click", function(){
	console.log('event bubbled up to body, NOOO');
});


//check off todos when clicked
$("ul").on("click", "li", function(){
	$(this).toggleClass("checkedOff");
});

//remove to do when "X"(span) is clicked on
$("ul").on("click", "span", removeTodo);

//adding a new todo
$("input[type='text']").on("keypress", newToDo);


function checkedOff(){
	$(this).toggleClass("checkedOff");
	return false;
	// event.stopPropagation();
}

function removeTodo(){
	$(this).parent().fadeOut(function(){
		$(this).remove();	
	})
	return false
	// event.stopPropagation();
}

function newToDo(){
	if(event.which === 13){
		$("ul").append(`<li><span><i class="fa fa-trash" aria-hidden="true"></i></span> ${$(this).val()}</li>`);
		$(this).val("");
	}
}