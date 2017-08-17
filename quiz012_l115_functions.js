// isEven() takes numbers and return true/false
function isEven(num) {
	if(num % 2 === 0) {
		return true
	}
	else {
		return false
	}
}

// factorial() takes a number and return its factorial
function factorial(num) {
	var factorial = 1;
	while(num > 1) {
		factorial = factorial * num;
		num--;
	}
	return factorial
}

// kebabToSnake() replace "-"s with "_"s in input string
function kebabToSnake(str) {
	while(str.indexOf("-") > 0) {
		str = str.replace("-", "_");
	}
	return str
}
