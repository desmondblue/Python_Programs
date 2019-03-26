'''
In a fair coin we have an equal chance (50%) of either getting a ‘head’ or ‘tail’.  
That is if we toss the coin a large number of times we would observe head approximately 50% of the time. 
Write a program to implement a biased coin toss where the chance of getting a head is 70% (and tail 30%).
That is if we invoke the program 1000 times we should see the head randomly approximately 700 times.
'''
from numpy import random
def toss():
    a = ["Tails","Heads"]
    
    value = random.choice(a,p=[0.3,0.7])
    return value
for i in range(10):
    print(toss())
