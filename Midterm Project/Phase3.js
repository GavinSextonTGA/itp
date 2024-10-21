function setup() {
    createCanvas(400, 400); // Set the size of canvas
    noStroke(); // Disable drawing the stroke
  }
  
  function drawObject(x, y, s) {
    push();
    translate(x, y);
    scale(s);
    fill(0); // Fill in with black color
    noStroke();
    ellipse(60, 60, 60, 60); // Draw ellipses 5x scale of drawing
    fill(255); // Fill in with white color
    rect(45, 30,  10, 60); // Draw rectangles
    rect(30, 65,  60, 5); 
    stroke(0);
    noFill();
    ellipse(60, 60, 60, 60);
    pop();
  }
  
  function draw() {
    drawObject(0, 0, 1);
    drawObject(0, 200, 1);
  }
  