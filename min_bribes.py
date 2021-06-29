#!/bin/python3
"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their 
initial position in the queue from  to . Any person can bribe the person directly in front of them to swap positions, but they 
still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if 
anyone has bribed more than two people, print Too chaotic.

Example

If person  bribes person , the queue will look like this: . Only  bribe is required. Print 1.
Person  had to bribe  people to get to the current position. Print Too chaotic.

"""


import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    count = 0
    q = [p-1 for p in q]
    for i, n in enumerate(q):
        if (n-i) > 2:
            print ("Too chaotic")                
            return
        for j in range(max(n-1,0),i):
            print ("q[%d] = %d and n = %d" %(j,q[j],n))
            if q[j] > n:
                count += 1
    print (count)           

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))
    
    minimumBribes(q)
    