# PHASE 1, Sketch
Going into this project I knew I had to keep my ambition low, as I really didn't want to get lost in complicated images and positions. 

I decided I would sketch the logo for the Super Smash Brothers series, a circle divided into 4 pieces with a cross.

## Dimensions
I started sketching a circle with a radius of five units, but I realized that increasing the dimensions to have a radius of 6 would make it both easier to scale and to match the original logo with the size of the white rectangles that divide the circle. 

I also decided that in order to keep the rectangles dividing it from being visable outside the circle, I wouldn't outline them but I would outline the circle
Overall while its certainly not ambitious, it at least looks like more shapes than it actually has which helps it not look too boring.


# PHASE 2, Translating to P5.js 
## First circle
Starting with copying and pasting the given code that makes 8th notes I had to decide on a scale for the image I had drawn. Luckily through the graph paper's clearly noted dimensions I was able to take a basic 12 by 12 circle and scale it up 5x to be 60 by 60 cuz I figured that was a nice round number.
## The rectangles
While I could have all at once looked up what each dimension did I understood it better by toying with each one individually, then I brought them to around where I thought they would end up and then finally added the exact dimensions to each rectangle to keep at the 5x scale.
## To stroke or not to stroke
I had already had a vague plan to have the whole circle stroke to outline the negative space created by the rectangles but I realized that that stroke was covered up when the rectangles were added. I ended up with an idea to create a second identical circle that wouldn't be filled in but would have the stroke, and leave everything else strokeless. Sadly this version very much relies on the background color also being white for now, otherwise the rectangles peak out. 

# Phase 3 Function
This phase didn't have as much decision making as the previous steps, it was moreso just me trying to understand the coorinates needed for the placement and scale of the drawing, understanding the meaning behind the push and pop functions, and remembering how functions are created and used within Javascript. Other than syntax errors there's nothing much to report on here. 

# Phase 4 Tiling (final boss)
## STEP ONE, Getting the Image correct
So throughout this I've been drawing the object a good way from where the x and y coordinates inputted would normally place it, so I had to do some basic coorinate changes to get it by default placed in the upper left corner. After screwing around with the circle first realizing it had to be at 30,30 rather than 60,60 the rectangles were easy to place in place. So the step that probably should have been done way earlier is complete yay.
## Step Two, Scaling
My goal is to get it set up so the image scales based off of the size of the grid needed, so for a 400 by 400 grid an inputted grid of 20 will have the image be 80 by 80 pixels rather than the 60 by 60 it is currently so it will be scaled by 1.33. Now how to represent this as scalable will require some algebra that I will do physically. 
### the algebra. 
Its a bit messy because its been years but I made x = grid size and s = scaling. I realized that 400/x would equal the number of pixels across that the image would have to be in order to fit correctly. I set that to be n, in case I needed it later. I then put some thought and I realized that 60 (the current size) times s would equal n. This let me bridge the gap in my mind and I came up with the equation 400/x=60s. After simplification and solving for s in order to be graphed I got 20/3x=s. Plugging it into desmos I got a sort of reverse exponential graph (its been so long since algebra)
The image from the graph is also in the midterm folder because putting an image into markdwon isn't what I want to be spending my time on right now. 
### implementing 
OH MY GOD I DID IT I THOUGHT IT WASN'T GOING TO WORK!!!!! 
I first made the last draw function call for the variable s instead of 1. I then allowed the grid size to be changed by editing variable g as it would be easier to read. Then I implemented my formula and it looked something like this: 
 g = 10;
  s = 20/(3 * g);
  function draw() {
    drawObject(0, 0, s);
  }
And by some miracle it works perfectly. I mean if I had to bug proof it I would set limits to what g could be, like equal or greater than 1 and less than or equal to 400 but those weren't required so I'll save myself the trouble. 
## TIling and nested loops. 
The first homework that required this I never ended up learning how to do it, so this is going to be fun..... so... 
## Reading the manual
While I did get the concept behind it, the syntax for the for loops was clearly displayed in Chapter 2 of the textbook, which was greatly appreciated. 
## Back to it 
Ok so I have an idea, the amount it counts for each new image (basically how far apart each one will be ) will be n (number of pixels ) from earlier, I'm glad I kept note of that. I'll see later how it will check when to move to the next line later but all things considered this is starting to seem possible and I'm excited. 
## the incident 
soooo.... turns out when you've got a for loop with no end condition it just crashes the site. I had been doing most adjustments on the website but i had luckily pasted it into phase4.js when I finished the scaling code so this actually isn't that bad of a setback, just an annoyance really. 
## Syntax shmintax
So I spent an hourish fighting over the syntax not understanding that the draw function had to be placed BEFORE the for loops, I even asked my roommate AJ and my girlfriend Adreanna and since it was a P5.js specific thing they couln't help me much, except for aj getting the syntax of the for loop's incrementing correctly because before I had it as x = x+n rather than x+=n. Even P5.js tried to explain to me to put the function on top but I couldn't understand what it meant by that. The code works by the way, its just the x for loop inside the y one and you can set any number within reason to g ( grid size) and it works. Also it turns out its really inneficient but I had the code working without butting the {} to make the y for loop functional, and I'm not sure why but it definitely run with less lag after adding the proper {}s. This has been a fun project and a lot of challenge. Goodnight!