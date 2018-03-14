// myForEach(array, function)

// js functions arguments are OPTIONAL?..
// as myForEach can be used without errors when given no args even tho
// they are defined to be used in the function

function myForEach(arr, func){
    for(var i = 0; i <= arr.length; i++){
        func(arr[i], i, arr);
    }
}

// ****** object method ******
// Array.prototype.myForEach = function(func){
//     for(var i = 0; i < this.length; i++){
//         func(this[i]);
//     }
// }
