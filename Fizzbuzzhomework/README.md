# fizz buzz
upon getting home from class and eating and doing my counterpoint homework I started searching around the class repository for how I was going to do the fizz buzz portion of the assignment
even understanding the counting function took some trial and error, though after messing around with the provided code I feel like i understand it way better
I changed the perameters and had a program that could count from 1 to 100, simple
Next using the remainder function provided I duplicated the code I had and had it print out its number again if it was divisible by 3 and an identical one for 5. 
After some annoying syntax errors it functioned pretty well. 
I set the 3 one to print "fizz" and the 5 one to print "buzz", now for the far more challenging ones, getting it to print its number only if it wasnt divisible by 5 and 3 and getting it to say "fizzbuzz" if it was divisible by both
I figured with some clever ordering this could be done as an if else statement, where it would only print the number if it didn't meet any of the previous perameters.
The problem was that else if espscially was really difficult for me to grasp in its syntax, I was constantly cross referencing it to the repository and catching small things I did wrong
Taking a break from that I made the fizzbuzz portion, which only responds if its divisible by both. I could have either checked if it was divisible by 15 or by both 3 and 5, I chose the latter to test out the && function. 
Ordering the fizzbuzz statement at the top meant the others would only display their string if it wasn't already divisible by both 3 and 5. I thought I needed 3 else statements for this.
The main syntax error remaining came from the first else if statemtent I put in after the fizzbuzz statement. I got upset and deleted the word else leaving it as an if statement... and it worked, well with printing fizzbuzz fizz, but it meant I had found my culprit for all of the damn errors
It turns out that i had the } on the wrong line, well probably more importantly before the ;. 
After a test and my program is a success. 


# Pyramid
After nearly a week after the last file I took some time to review the code displayed on last week's readme, I refreshed my memory.
The pyramid looked easy enough, as the range was restricted between 1 and 8, so I could easily just tell the computer to display a number of lines of the "image" equal to the mumber displayed which could be done easily with the > and < operators, after copy pasting the input code from BOSeasons.js first of course  
The one hurdle remaining was remembering the line breaks, though that was just a quick google and I don't have to credit a basic funciton right? I mean here it is I guess [(https://www.w3schools.com/js/js_strings.asp)]
And after adding restrictions on what values could be added the project was complete


# Chessboard
I am still stumped on this one, 
I had an idea to start, just getting it to count down from the number inputted and subtract that by one to match the amount of lines as the number inputed, but this did not account for changing the amount of #s. 
After trial and error I did get it functioning though, the top code is that, it can creat any chessboard... thats dimensions are x by 8 
I couldn't find where else to take that idea so I tried again with a for loop but I couldn't figure out how to check the value of i during excecution to know whether it shoud start on a # or a space. 
I have concepts of a plan on what else I could do, but counting how many symbols its displaying and then knowing when to break the line is something I can't do

I think there was a funciton related to this that was hinted at in class but I quadruple checked the repository and found nothing so it was no use.