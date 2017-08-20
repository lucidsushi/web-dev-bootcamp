function todo_list(){
	var todo = prompt("What would you like to do?");
	var todos = [];

	while(todo !== "quit"){
		if(todo === "new"){
			var new_todo = prompt("Eneter a new todo");
			todos.push(new_todo);
		} else {
			console.log(todos);
		}
	}	
}


todo_list();