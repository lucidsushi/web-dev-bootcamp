var rgbGameDisplay = document.getElementById('rgbGameDisplay');
var resetBtn = document.getElementById('resetColors');
var modeBtns = document.querySelectorAll(".modeBtn");
var squares = document.querySelectorAll(".square");
var hintBtn = document.getElementById('hintBtn');
var hint = document.getElementById('hint');
var correctColor = {index: null, color: null};
var RESET_BTN_OPTIONS = {NEW_COLORS: "New Colors", PLAY_AGAIN: "Play Again?"};
var numSquares = {current: 6};


function initialize(){
  modeBtns[1].classList.add("selected");
  resetBtn.addEventListener("click", newGame);
  hintBtn.addEventListener("mouseover", toggleHintVis);
  hintBtn.addEventListener("mouseout", toggleHintVis);
  hintBtn.addEventListener("click", toggleHintVis);

  for(var i = 0; i < modeBtns.length; i++){
    modeBtns[i].addEventListener("click", modeBtnEvent);
  }
  newGame();
}

function newGame(){
  var resultDisplay = document.getElementById('resultDisplay');

  correctColor.index = Math.floor(Math.random() * numSquares.current);
  rgbGameDisplay.style.backgroundColor = "steelblue";
  resultDisplay.textContent = "";
  resetBtn.value = RESET_BTN_OPTIONS.NEW_COLORS;

  for(var i = 0; i < 6; i++){
    var rgb = randomRgb();
    if(i === correctColor.index){
      correctColor.color = rgb;
      document.getElementById('rgbDisplay').textContent = correctColor.color;
    }
    if(i < numSquares.current){
      squares[i].style.display = "";
      squares[i].style.backgroundColor = rgb;
      squares[i].addEventListener("click", evalChoice.bind(squares[i],
                                                           resultDisplay));
    } else {
      squares[i].style.display = "none";
    }
  }
}

function modeBtnEvent(){
  //mode = Easy or else(Hard)
  modeBtns[0].classList.remove("selected");
  modeBtns[1].classList.remove("selected");
  this.classList.add("selected");
  numSquares.current = (this.value === "Easy") ? 3 : 6;
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

function evalChoice(resultDisplay){
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
    resetBtn.value = RESET_BTN_OPTIONS.PLAY_AGAIN;

    //all squares change color to correct color
    rgbGameDisplay.style.backgroundColor = correctColor.color;
    for(var i = 0; i < squares.length; i++){
      squares[i].style.backgroundColor = correctColor.color;
    }
}


initialize();