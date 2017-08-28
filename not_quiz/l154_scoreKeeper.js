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
	p1Count.style.color = "black";
	p2Count.style.color = "black";
	pCounts.forEach(function(pCount){
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