
var serial;
function preload() {
  var dir =   'serial_data.json';
  serial = loadJSON(dir);
}

var img;

function setup() {
  //setup
  createCanvas(600,1000);
  background(50);
  noSmooth();
  // for(var x = 0; x < 0; x++) {
  //   for(var y = 0; y < 0; y++) {
  // // for(var i = startx, endx)
  // // for(var j starty, endy)
  //   moveRobot(x,y);
  //   img_data[x][y] = readSerialVal();
  // // }
  // // }
  //     }
  //   }
    
  img = imageRender(serial.data,1,serial['data'][0].length);
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

//todo
//[] add heatmap
//[] add error checking if datastructure has ONLY 'numbers'
//https://www.patrick-wied.at/static/heatmapjs/
// demo
// https://www.patrick-wied.at/static/heatmapjs/example-minimal-config.html
//datastruct object, width of datastruct, height of datastruct
function imageRender(d, w,h){
  var i = createImage(w,h);
  i.loadPixels();
  for(var x = 0; x < i.width; x++) {
    for(var y = 0; y < i.height; y++) {
      var r = map(y, 0, i.height, 255, 0);
      
      
      //color
      var c = d[x][y];
       c = map(c,220,370,1,255);
      //x,y position, r,g,b values, alpha(aka opasity)
      i.set(x,y, [c, c,c,255]);
    }   
  }
  i.updatePixels();
  return i;
}