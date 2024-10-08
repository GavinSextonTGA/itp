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

