

var img_data = [[255,1,255,1,255,1,255,1,255,1,255,1,255,1,255,1,255,1,255,1,255,1,255,1],
[255,1,255,1,255,1,255,1,255,1,255,1,255,1,255,1,255,1,255,1,255,1,255,1],
[255,1,255,1,255,1,255,1,255,1,255,1,255,1,255,1,255,1,255,1,255,1,255,1]];
var img;

function setup() {
  //setup
  createCanvas(600,600);
  background(50);
  
  for(var x = 0; x < 0; x++) {
    for(var y = 0; y < 0; y++) {
  // for(var i = startx, endx)
  // for(var j starty, endy)
    moveRobot(x,y);
    img_data[x][y] = readSerialVal();
  // }
  // }
      }
    }
  
  img = renderImage(img_data,3,24);
}

function draw() {
  background(50);
  image(img,100,100);
  
  
}

function moveRobot(x,y){
  //todo
}

function readSerialVal(){
  //todo
}

//todo add heatmap
//https://www.patrick-wied.at/static/heatmapjs/
//datastruct object, width of datastruct, height of datastruct
function renderImage(d, w,h){
  var i = createImage(w,h);
  i.loadPixels();
  for(var x = 0; x < i.width; x++) {
    for(var y = 0; y < i.height; y++) {
      var r = map(y, 0, i.height, 255, 0);
      //color
      var c = d[x][y];
      
      //x,y position, r,g,b values, alpha(aka opasity)
      i.set(x,y, [c, c,c,255]);
    }   
  }
  i.updatePixels();
  return i;
}