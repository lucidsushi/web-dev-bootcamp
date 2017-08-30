var rgbDisplay = document.querySelector("#rgbDisplay");
var squares = document.querySelectorAll(".square");
var rgbGameDisplay = document.querySelector("#rgbGameDisplay");
var resultDisplay = document.querySelector("#resultDisplay");
var newColorsBtn = document.querySelector("#resetColors");
var rightAnswer = {index: null, answer: null};
var newColorsBtnOptions = {newcolors: "New Colors", playagain: "Play Again?"}


function initialize(){
  newColorsBtn.value = newColorsBtnOptions.newcolors;
  rightAnswer["index"] = getAnswerIndex();

  rgbGameDisplay.style.backgroundColor = "rgb(25, 25, 25)";
  newColorsBtn.addEventListener("click", initialize);

  for(var i = 0; i < squares.length; i++){
    var rgb = randomRgb();
    if(i === rightAnswer["index"]){
      rightAnswer["answer"] = rgb;
    }
    rgbDisplay.textContent = rightAnswer["answer"];
    squares[i].style.backgroundColor = rgb;
    squares[i].addEventListener("click", evalChoice);
  }
}

function getAnswerIndex(){
  return Math.floor(Math.random() * 6);
}

function randomRgb(){
  var rgbList = [];
  for(var i = 0; i < 3; i++){
    rgbList.push(Math.floor(Math.random() * 256));
  }
  var rgb = `rgb(${rgbList[0]}, ${rgbList[1]}, ${rgbList[2]})`;
  return rgb;
}

function evalChoice(){
  if(this.style.backgroundColor === rightAnswer["answer"]){
    resultDisplay.textContent = "You've guessed correctly!";
    resultRightAnswer();
  } else {
    resultDisplay.textContent = "Wrong guess, try again!";
    this.style.backgroundColor = "rgb(25, 25, 25)";
  }
}

function resultRightAnswer(){
    //button text change
    newColorsBtn.value = newColorsBtnOptions.playagain;

    //color change
    rgbGameDisplay.style.backgroundColor = rightAnswer["answer"];
    for(var i = 0; i < squares.length; i++){
      squares[i].style.backgroundColor = rightAnswer["answer"];
    }
}


initialize();