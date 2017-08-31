var rgbDisplay = document.querySelector("#rgbDisplay");
var squares = document.querySelectorAll(".square");
var rgbGameDisplay = document.querySelector("#rgbGameDisplay");
var resultDisplay = document.querySelector("#resultDisplay");
var resetBtn = document.querySelector("#resetColors");
var hardBtn = document.querySelector("#hardBtn");
var easyBtn = document.querySelector("#easyBtn");
var correctColor = {index: null, color: null};
var resetBtnOptions = {newcolors: "New Colors", playagain: "Play Again?"};
var numSquares = {current: 6};


function newGame(){
  rgbGameDisplay.style.backgroundColor = "steelblue";
  resultDisplay.textContent = "";
  resetBtn.value = resetBtnOptions.newcolors;

  correctColor.index = Math.floor(Math.random() * numSquares.current);

  resetBtn.addEventListener("click", newGame);
  easyBtn.addEventListener("click", easyBtnEvent);
  hardBtn.addEventListener("click", hardBtnEvent);

  for(var i = 0; i < 6; i++){
    var rgb = randomRgb();
    if(i === correctColor.index){
      correctColor.color = rgb;
    }
    rgbDisplay.textContent = correctColor.color;
    if(i < numSquares.current){
      squares[i].style.display = "";
      squares[i].style.backgroundColor = rgb;
      squares[i].addEventListener("click", evalChoice);
    } else {
      squares[i].style.display = "none";
    }
  }
}

function easyBtnEvent(){
  this.classList.add("selected");
  hardBtn.classList.remove("selected");
  numSquares.current = 3;
  newGame();
}

function hardBtnEvent(){
  this.classList.add("selected");
  easyBtn.classList.remove("selected");
  numSquares.current = 6;
  newGame();
}

function randomRgb(){
  var rgbList = [];
  for(var i = 0; i < 3; i++){
    rgbList.push(Math.floor(Math.random() * 256));
  }
  return `rgb(${rgbList[0]}, ${rgbList[1]}, ${rgbList[2]})`;
}

function evalChoice(){
  if(this.style.backgroundColor === correctColor.color){
    resultDisplay.textContent = "You've guessed correctly!";
    gameComplete();
  } else {
    resultDisplay.textContent = "Wrong guess, try again!";
    this.style.backgroundColor = "rgb(25, 25, 25)";
  }
}

function gameComplete(){
    //button text change
    resetBtn.value = resetBtnOptions.playagain;

    //color change
    rgbGameDisplay.style.backgroundColor = correctColor.color;
    for(var i = 0; i < squares.length; i++){
      squares[i].style.backgroundColor = correctColor.color;
    }
}


newGame();