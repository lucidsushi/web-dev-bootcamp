// button = document.querySelector("button");
// button.addEventListener("click", function(){
// 	// document.querySelector("body").classList.toggle("toggleColor");
// 	document.body.classList.toggle("toggleColor");
// });

p1 = document.querySelector("#p1");
p2 = document.querySelector("#p2");
p1Count = document.querySelector("#p1Count");
p2Count = document.querySelector("#p2Count");
scoreMax = document.querySelector("#scoreMax");
reset = document.querySelector("#reset");

p1.addEventListener("click", addOneTo.bind(null, p1Count));
p2.addEventListener("click", addOneTo.bind(null, p2Count));
reset.addEventListener("click", resetCount.bind(null, [p1Count, p2Count]));

function addOneTo(pCount){
	pCount.textContent = parseInt(pCount.textContent) + 1;
}

function resetCount(pCounts){
	pCounts.forEach(function(pCount){
		pCount.textContent = 0;
	});
}
