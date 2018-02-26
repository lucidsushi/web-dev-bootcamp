// isEven() takes numbers and return true/false
function isEven(num){
	// if(num % 2 === 0) {
	// 	return true
	// }
	// else {
	// 	return false
	// }
	return num % 2 === 0;
}

// factorial() takes a number and return its factorial
function factorial(num){
	// while(num > 1) {
	// 	// factorial = factorial * num;
	// 	factorial *= num;
	// 	num--;
	// }
	var result = 1;
	for(var i = 2; i <= num; i++){
		result *= i;
	}
	return result;
}

// kebabToSnake() replace "-"s with "_"s in input string
function kebabToSnake(str){
	// while(str.indexOf("-") > 0) {
	// 	str = str.replace("-", "_");
	// }
	return str.replace(/-/g, "_");

}
