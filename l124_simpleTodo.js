function todoList(){
    var option = undefined;
    var todos = [];

    while(option !== "quit"){
        var option = prompt("Enter an option: \
                             (new, delete, list or quit)");
        option = option.toLowerCase();
        if(option === "new"){
            newTodo(todos);
        } else if(option === "list"){
            listTodo(todos);
        } else if(option === "delete"){
            deleteTodo(todos);
        }
    }//while loop
}

function newTodo(todos){
    var todo = prompt("Enter a new todo...");
    todos.push(todo);
    console.log(todo + " added to todo list.");
}

function listTodo(todos){
    var visualTodo = visualizeTodos(todos);
    console.log(visualTodo);
    alert(visualTodo);
}

function deleteTodo(todos){
    //ask for index of item to delete and delete it from todos
    var visualTodo = visualizeTodos(todos);
    var index_to_delete = prompt("Enter index of item to delete:\n"
                                 + visualTodo);
    alert(todos[index_to_delete] + " is removed.");
    todos.splice(index_to_delete, 1);
}

function visualizeTodos(todos){
    //return a block string visualizing todo list
    visualTodo = "**********\n";
    todos.forEach(function(todo, index){
        visualTodo += index + " : " + todo + "\n";
    })
    visualTodo += "**********\n";
    return visualTodo;
}

todoList();