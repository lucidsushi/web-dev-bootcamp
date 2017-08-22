// printReverse() - take an array and return each element one at a time in
// reverse order
function printReverse(array){
    var loopSize = array.length;
    for(var i=0; i<loopSize; i++){
        console.log(array.pop());
    }
}

// isUniform() - take an array and return true if all elements are the same,
// otherwise return false
function isUniform(array){
    var element = array.pop();
    var uniform = true;
    array.forEach(function(val){
        if(val !== element){
            uniform = false;
        }
    })
    return uniform;
}

// sumArray() - take an array of numbers and return the sum of the numbers
function sumArray(array){
    var sum = 0;
    array.forEach(function(val){
        sum += val;
    })
    return sum;
}

// max() - take an array and return the maximum number
function max(array){
    max = array.pop();
    array.forEach(function(val){
        if(val >= max){
            max = val;
        }
    })
    return max;
}
