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
var pCounts = [p1Count, p2Count];
var p1score = 0;
var p2score = 0;
var gameover = false;

p1.addEventListener("click", manageCount.bind(null, p1Count, p1score));
p2.addEventListener("click", manageCount.bind(null, p2Count, p2score));
scoreMaxManual.addEventListener("input", alterScoreMax);
reset.addEventListener("click", resetCount.bind(null, pCounts));

function alterScoreMax(){
	scoreMax.textContent = this.value;
}

function resetCount(pCounts){
	pCounts.forEach(function(pCount){
		pCount.style.color = "black";
		pCount.textContent = 0;
		p1score = 0;
		p2score = 0;
	});
}

function manageCount(pCount, pScore){
	pScore += 1;

	if(pScore === parseInt(scoreMax.textContent)){
		console.log("max is reached")
		gameover = true;
		pCount.style.color = "greenyellow";
	}
	if(!gameover){
		console.log("not game over yet");
		pCount.textContent = pScore;
	}
}

resetCount(pCounts);