#!/bin/python

import math
import os
import random
import re
import sys

# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20 , print Not Weird

if __name__ == '__main__':
  if __name__ == '__main__':
    n = int(raw_input().strip())
    is_even= n % 2 == 0
    if n >=2 and n <=5 and is_even:
        print ("Not Weird")
    elif n >=6 and n <=20 and is_even:
        print ("Weird") 
    elif n >20 and is_even:
        print ("Not Weird")        
    elif n % 2 == 1:
        print ("Weird")