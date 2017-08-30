var rgbDisplay = document.querySelector("#rgbDisplay");
var squares = document.querySelectorAll(".square");
var rightAnswer = {answer: getAnswerSeed()};

for(var i = 0; i < squares.length; i++){
  var rgb = randomRgb();
  if(i === rightAnswer["answer"]){
    rightAnswer["answer"] = rgb;
  }
  squares[i].style.backgroundColor = rgb;
  squares[i].addEventListener("click", evalChoice);
}

rgbDisplay.textContent = rightAnswer["answer"];

function getAnswerSeed(){
  return Math.floor(Math.random() * 5);
}

function randomRgb(){
  var rgbList = [];
  for(var i = 0; i < 3; i++){
    rgbList.push(Math.floor(Math.random() * 256));
  }
  var rgb = "rgb(" + rgbList[0] + ", " + rgbList[1] + ", " + rgbList[2] + ")";
  return rgb;
}

function evalChoice(){
  if(this.style.backgroundColor === rightAnswer["answer"]){
    console.log("correct guess");
  } else {
    console.log("incorrect guess");
  }
}



