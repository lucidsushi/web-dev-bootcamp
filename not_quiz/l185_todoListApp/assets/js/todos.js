// event bubbling check
$("body").on("click", function(){
	console.log('event bubbled up to body, NOOO');
});

//adding a new todo
$("input[type='text']").on("keypress", newToDo);

//check off todos when clicked
$("ul").on("click", "li", checkedOff);

//remove to do when "X"(span) is clicked on
$("ul").on("click", ".removeLi", removeTodo);

// //edit a current todo
// $("ul").on("click", ".editLi", editTodo);

function newToDo(event){
	if(event.which === 13){
		$("ul").append(`<li>
							<span class="removeLi">
								<i class="fa fa-trash" aria-hidden="true"></i>
							</span>
							${$(this).val()}
						</li>`);
		$(this).val("");
	}

	event.stopPropagation();
}

function checkedOff(event){
	$(this).toggleClass("checkedOff");
	event.stopPropagation();
}

function removeTodo(event){
	$(this).parent().fadeOut(function(){
		$(this).remove();
	})
	event.stopPropagation();
}

