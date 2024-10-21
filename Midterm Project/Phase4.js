function setup() {
    createCanvas(400, 400); // Set the size of canvas
    noStroke(); // Disable drawing the stroke
  background(255);
  
  }
function drawObject(x, y, s) {
    push();
    translate(x, y);
    scale(s);
    fill(0); // Fill in with black color
    noStroke();
    ellipse(30, 30, 60, 60); // Draw ellipses 5x scale of drawing
    fill(255); // Fill in with white color
    rect(12, 0,  10, 60); // Draw rectangles
    rect(0, 35,  60, 5); 
    stroke(0);
    noFill();
    ellipse(30, 30, 60, 60);
    pop();
  }
  g = 20; // grid size
  s = 20/(3 * g); // scaling number
  n = 60 * s; // height and width of image after scaling
function draw(){
  for (let y = 0; y <= 400; y += n)  {
    for (let x = 0; x <= 400; x += n) {
      drawObject(x, y, s);
    }
  }  
}