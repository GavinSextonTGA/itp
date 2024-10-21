
function setup() {
  createCanvas(150, 150); // Set the size of canvas
   // Disable drawing the stroke
}

function draw() {
  fill(0); // Fill in with black color
  noStroke();
  ellipse(60, 60, 60, 60); // Draw ellipses 5x scale of drawing


  fill(255); // Fill in with white color
  
  rect(45, 30,  10, 60); // Draw rectangles
  rect(30, 65,  60, 5); 
  stroke(0);
  noFill();
  ellipse(60, 60, 60, 60);
 
}