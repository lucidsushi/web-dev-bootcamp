function todo_list(){
	var option = undefined;
	var todos = [];

	while(option !== "quit"){
		var option = prompt("What would you like to do? \
							 (new, delete, list or quit)");
		if(option === "new"){
			var new_todo = prompt("Enter a new todo...");
			todos.push(new_todo);
			console.log(new_todo + " added to todo list.");
		} else if(option === "list"){
			var visual_todo = visualize_todos(todos);
			console.log(visual_todo);
			alert(visual_todo);
		} else if(option === "delete"){
			delete_todo(todos);
		}
	}//while loop
}

function visualize_todos(todos){
	//return a block string visualizing todo list
	visual_todo = "**********\n";
	todos.forEach(function(todo, index){
		visual_todo += index + " : " + todo + "\n";
	})
	visual_todo += "**********\n";
	return visual_todo;
}

function delete_todo(todos){
	var visual_todo = visualize_todos(todos);
	var index_to_delete = prompt("Enter index of item to delete:\n"
								 + visual_todo);
	alert(todos[index_to_delete] + " is removed.");
	todos.splice(index_to_delete, 1);
}

todo_list();