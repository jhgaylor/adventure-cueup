Level 1:
I spent most of my time in level 1 learning about LCG and in particular a function called MTH$RANDOM.  I toyed with altering the math inside of the function by changing the value of m to 36 but got crazy results.  I settled on % 36 meaning do modulos 36 on the MTH$RANDOM return value.  

The math was straight forward, but since I didn't know what an LCG was (I just knew the numbers were pseudo random) I definitely didn't know how to implement one.  I googled Vax and MTH$RANDOM, read the wikipedia article to get some domain knowledge, and then started looking for some source code.  I found an implementation of Vax in c, so I read through it and reimplemented it in python.

Seeding the Vax algorithm with 6 will return the cyclic pattern of the roulette machine.  The game records me there for over 5 hours but I made dinner and did other unrelated work in between.  I'd say I spend roughly 60 minutes working on the problem.  90 max.