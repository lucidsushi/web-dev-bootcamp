var age = Number(prompt("What is your age?"));

if(age < 0) {
	console.log("Error: age cannot be a negative number");
}

else if(age === 21) {
	console.log("happy 21st birthday!");
}

else if(age % 2 === 1) {
	console.log("your age is odd!");
}

else if((age ** 0.5) ** 2 === age) {
	console.log("perfect square!");
}

else if(age < 18) {
	console.log("Sorry, you are not old enough to enter the venue");
}

else if(age < 21) {
	console.log("You can enter, but cannot drink");
}

else {
	console.log("Come on in. You can drink.")
}

// probably wanna use these intead for the future
// Math.pow()
// Math.sqrt()