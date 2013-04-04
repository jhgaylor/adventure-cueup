Level 1:

I spent most of my time in level 1 learning about LCG and in particular a function called MTH$RANDOM.  I toyed with altering the math inside of the function by changing the value of m to 36 but got crazy results.  I settled on % 36 meaning do modulos 36 on the MTH$RANDOM return value.  

The math was straight forward, but since I didn't know what an LCG was (I just knew the numbers were pseudo random) I definitely didn't know how to implement one.  I googled Vax and MTH$RANDOM, read the wikipedia article to get some domain knowledge, and then started looking for some source code.  I found an implementation of Vax in c, so I read through it and reimplemented it in python.

Seeding the Vax algorithm with 6 will return the cyclic pattern of the roulette machine.  The game records me there for over 5 hours but I made dinner and did other unrelated work in between.  I'd say I spend roughly 60 minutes working on the problem.  90 max.


Level 2:

I spent fighting the computer... because I had faulty logic.  My logic happened to coincide closely with the solution because I was counting the number of opened and closed containers and the solution was near the edge.
I found the correct solution by putting open symbols on a stack and popping a symbol off when I found a close symbol.  If the symbols didn't match I knew I found a solution.  My index was spot on this time.  I took out the new lines when copying the input to my python script, but I added a .replace("\n", "") to show how I'd have dealt with the new lines.

Level 3: (identical to level3.md)

I just thought this one through.

I took the cost of the last move out of the equation. Meaning I had 30 tokens to land on the 4 or 8.

The minimum number of moves to get from * to the 4 or 8 was 8.  The average cost of the 8 moves was 3.75.

The board required taking an 8 which counted for more than 2 moves. Looking at the map I noted a path through the one that summed to 29, and then one to 27.  At this point I tried to wrap around the map even though the directions led me to believe it was not possible (mentioned falling off the map).  Thinking about wrapping let me to think about repeating a move.  the path that summed to 27 already passed through the 1 next to the 2.  The solution was pretty obvious from here.

If I had to guess how I'd implement this, I'd probably start with decision trees.