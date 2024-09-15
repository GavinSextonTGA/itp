# Scratch Project Notes
## Gavin Sexton 
After opening Scratch and looking through the tutorials and examples provided I decided I wanted to make some sort of game
Obviously I knew programming moving platforms and collision and gravity would be way too ambitious for my first time trying to code ever, so I had to browse the sprites for some inspiration for an easier goal to fulfill 
Upon looking for sprites I found my fatefull protagonist, the man the myth the legend... frank
I didn't know what kind of game I wanted to to be so I just decided to mess with movement for frank. The most obvious first step would be using the first function available for movement, steps
But upon testing it out the step function relied on rotation and I didn't want to deal with that, so I found the much more intuitive function changing the x position of frank by 30 each time i pressed an arrow in a direction 
Though I didn't like that he just kind of teleported 30 units in each direction so I added a gradual motion by making him move by 10 3 times in a row, though I'll be honest the controls are still clunky
I thought that a simple game that could be made with my limited programming knowledge would be a collecting game, its very easy to implement and it reminded me of a mario party minigame
I found franks fated sustinence, a scrumptious taco, I had made guacamole and pico de gallo earlier that day
I set up functions to define the taco and franks position upon the starting of the game
Scratch has a really dumbed down collision detecter so setting up the taco to realize that it has been in contat with frank or the floor was easy, and i set some very advanced falling code along with it
I was amazed at the size function and decided that frank would be growing stronger due to the power of the tacos
I set up a thing that would tell frank to grow when collision with the taco was detected and wouldnt when the floor was in contact with the taco
I made the taco disapear when in contact
I decided that frank would need a lot more tacos, i originally had 10 of them with copied code all along and calling eachother when they got in contact
I remembered that sometimes a lot of objects call upon some parent code or something to improve efficiency, though i could not find that feature explicitly in scratch
Upon setting up the calling code i accidentally had 1 taco call itself over and over again
I realized i was being a dumb dumb by making 10 different tacos so i reduced it to 2, 1 that spawns when you start the game, and 1 that spawns when a taco hits something 
upon running the code i witnessed franks massive increase in size and I thought it was really funny how once he grew to the y value where the tacos were spawning he would fly away majestically due to me also making him go up every time he got a taco to combat the sprite growing into the invisible floor where frank resides
I decided that this bug was now intended and was the games true ending
I added a variable to count the tacos frank consumed and when it got to 20 it would despawn frank and the tacos and make an explosion for frank had eaten too much too quickly
I encountered a weird problem, despite me telling it to raise the tacos eaten variable to increase it was not doing so
Upon consulting my girlfriend she told me it was due to the tacos disapearing before the variable was modified. I modified the code to only disapear after it changed the variable and sure enough it worked
all that was left was to add some sound effects when the tacos were collected and draw a beautifully rendered explosion for the games final ending
I added a background and cleaned up the random blocks i had left on screen and my very cool and very original game was compl
 
