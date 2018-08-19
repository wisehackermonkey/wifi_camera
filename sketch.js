var img_data = [[]];
var img;

function setup() {
  //setup
  createCanvas(600,600);
  background(50);
  img = createImage(400,400);
 
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
  
  
  
  img.loadPixels();
  for(var x = 0; x < img.width; x++) {
    for(var y = 0; y < img.height; y++) {
      var r = map(y, 0, img.height, 255, 0);
      img.set(x,y, [r,255-r,0,255]);
    }   
  }
  img.updatePixels();

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