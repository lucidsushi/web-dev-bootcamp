function todo_list(){
	var todo = undefined;
	var todos = [];

	while(todo !== "quit"){
		var todo = prompt("What would you like to do? (new, list or quit)");
		if(todo === "new"){
			var new_todo = prompt("Enter a new todo..");
			todos.push(new_todo);
		} else if(todo === "list"){
			alert(todos);
		}
	}	
}

todo_list();