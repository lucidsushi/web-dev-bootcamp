// button = document.querySelector("button");
// button.addEventListener("click", function(){
// 	// document.querySelector("body").classList.toggle("toggleColor");
// 	document.body.classList.toggle("toggleColor");
// });


playerOne = document.querySelector("#p1");
playerTwo = document.querySelector("#p2");
reset = document.querySelector("#reset");
playerOne.addEventListener("click", addOneTo);
playerTwo.addEventListener("click", addOneTo);
reset.addEventListener("click", function(){
	document.querySelector("#p1Count").textContent = 0;
	document.querySelector("#p2Count").textContent = 0;
});

function addOneTo(){
	//add 1 score to player one/two
	counterSelector = "#" + this.id + "Count";
	counter = document.querySelector(counterSelector);
	counter.textContent = parseInt(counter.textContent) + 1;
}
