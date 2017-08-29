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
var pCounts = [p1Count, p2Count];
var pScores = {p1: 0, p2: 0};
var gameover = false;

p1.addEventListener("click", manageCount.bind(null, p1Count, pScores, "p1"));
p2.addEventListener("click", manageCount.bind(null, p2Count, pScores, "p2"));
scoreMaxManual.addEventListener("input", alterScoreMax);
reset.addEventListener("click", resetCount.bind(null, pCounts));

function manageCount(pCount, pScores, pKey){
	if(!gameover){
		pScores[pKey] += 1;
		pScore = pScores[pKey];

		if(pScore >= Number(scoreMax.textContent)){
			gameover = true;
			pCount.classList.add("gameOverColor");
		}
		pCount.textContent = pScore;
	}
	
}

function alterScoreMax(){
	alteredValue = this.value;
	if(alteredValue > 0){
		scoreMax.textContent = alteredValue;	
	}	
}

function resetCount(pCounts){
	pCounts.forEach(function(pCount){
		pCount.textContent = 0;
		pScores["p1"] = 0;
		pScores["p2"] = 0;
	});
	p1Count.classList.remove("gameOverColor");
	p2Count.classList.remove("gameOverColor");
	gameover = false;
}

resetCount(pCounts);