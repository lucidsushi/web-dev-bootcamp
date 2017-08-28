/*
- one counter between player 1 and 2 changes color when reaching max score
- player 1 and 2 buttons no longer adds to count when reaching max score
- number input changes max score
- reset button resets count back to zero (and color changes) but does not have to reset max score input/display, at this point player buttons adds scores again
*/
var p1 = document.querySelector("#p1");
var p2 = document.querySelector("#p2");
var p1Count = document.querySelector("#p1Count");
var p2Count = document.querySelector("#p2Count");
var scoreMax = document.querySelector("#scoreMax");
var scoreMaxManual = document.querySelector("#scoreMaxManual");
var reset = document.querySelector("#reset");
//bind returns a new function object
var manageCountBindP1 = manageCount.bind(null, p1Count);
var manageCountBindP2 = manageCount.bind(null, p2Count);
var pCounts = [p1Count, p2Count];

scoreMaxManual.addEventListener("input", alterScoreMax);
reset.addEventListener("click", resetCount.bind(null, pCounts));

function alterScoreMax(){
	scoreMax.textContent = this.value;
}

function resetCount(pCounts){
	p1.addEventListener("click", manageCountBindP1);
	p2.addEventListener("click", manageCountBindP2);
	pCounts.forEach(function(pCount){
		pCount.style.color = "black";
		pCount.textContent = 0;
	});
}

function manageCount(pCount){
	var numCount = parseInt(pCount.textContent);
	pCount.textContent = numCount + 1;
	//scoreMax reached
	if(pCount.textContent === scoreMax.textContent){
		pCount.style.color = "greenyellow";
		p1.removeEventListener("click", manageCountBindP1);
		p2.removeEventListener("click", manageCountBindP2);
	}
}

resetCount(pCounts);