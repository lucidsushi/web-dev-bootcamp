var squares = document.querySelectorAll(".square");


function randomRgb(){
  var rgbList = []
  for(i = 0; i < 3; i++){
    rgbList.push(Math.floor(Math.random() * 256));
  }
  rgb = "rgb(" + rgbList[0] + ", " + rgbList[1] + ", " + rgbList[2] + ")";
  return rgb;
}