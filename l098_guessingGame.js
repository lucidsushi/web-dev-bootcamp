var number = Number(prompt("Guess a number"));

var secretNumber = 4;



if(number === secretNumber) {
	alert("You got it right!")
}

else if(number > secretNumber) {
	alert("You guessed too high!")
}

else {
	alert("You guessed too low!")
}