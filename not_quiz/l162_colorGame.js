var rgbGameDisplay = document.querySelector("#rgbGameDisplay");
var rgbDisplay = document.querySelector("#rgbDisplay");
var resultDisplay = document.querySelector("#resultDisplay");
var resetBtn = document.querySelector("#resetColors");
var modeBtns = document.querySelectorAll("#modeBtn");
var squares = document.querySelectorAll(".square");
var hintBtn = document.querySelector("#hintBtn");
var hint = document.querySelector("#hint");
var correctColor = {index: null, color: null};
var resetBtnOptions = {newcolors: "New Colors", playagain: "Play Again?"};
var numSquares = {current: 6};


function newGame(){
  correctColor.index = Math.floor(Math.random() * numSquares.current);
  rgbGameDisplay.style.backgroundColor = "steelblue";
  resultDisplay.textContent = "";
  resetBtn.value = resetBtnOptions.newcolors;

  addBtnEvents();

  for(var i = 0; i < 6; i++){
    var rgb = randomRgb();
    if(i === correctColor.index){
      correctColor.color = rgb;
      rgbDisplay.textContent = correctColor.color;
    }
    if(i < numSquares.current){
      squares[i].style.display = "";
      squares[i].style.backgroundColor = rgb;
      squares[i].addEventListener("click", evalChoice);
    } else {
      squares[i].style.display = "none";
    }
  }
}

function addBtnEvents(){
  resetBtn.addEventListener("click", newGame);
  hintBtn.addEventListener("mouseover", toggleHintVis);
  hintBtn.addEventListener("mouseout", toggleHintVis);
  hintBtn.addEventListener("click", toggleHintVis);

  for(var i = 0; i < modeBtns.length; i++){
    modeBtns[i].addEventListener("click", modeBtnEvent);
  }
}

function modeBtnEvent(){
  //mode = Easy or else(Hard)
  modeBtns[0].classList.remove("selected");
  modeBtns[1].classList.remove("selected");
  this.classList.add("selected");
  this.value === "Easy" ? numSquares.current = 3 : numSquares.current = 6;
  newGame();
}

function toggleHintVis(){
  hint.classList.toggle("toggleDisplay");
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
    resultDisplay.textContent = "CORRECT!";
    gameComplete();
  } else {
    resultDisplay.textContent = "WRONG PICK.. TRY AGAIN!";
    this.style.backgroundColor = "rgb(25, 25, 25)";
  }
}

function gameComplete(){
    //button text change to play again
    resetBtn.value = resetBtnOptions.playagain;

    //all squares change color to correct color
    rgbGameDisplay.style.backgroundColor = correctColor.color;
    for(var i = 0; i < squares.length; i++){
      squares[i].style.backgroundColor = correctColor.color;
    }
}


newGame();