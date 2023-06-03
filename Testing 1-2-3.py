'''Testing 1-2-3
7 kyu
Python

DESCRIPTION:
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

Tags: 
  ARRAYS
  FUNDAMENTALS
'''


# solution 1
def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]
 
 
 # solution 2
 def number(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]
 
 
 # solution 3
 def number(lines):
    return ['{}: {}'.format(n, s) for (n, s) in enumerate(lines, 1)]
   
  
  # Solution 4
  def number(lines):
    return ["{0}: {1}".format(i + 1, lines[i]) for i in xrange(len(lines))]
  
  
  # Solution 5
  def number(lines):
    #your code here
    a=[]
    for i,c in enumerate(lines,1):
        str_var = str(i) + ': ' + str(c) #make sure to add another space
        a.append(str_var)
    return a
  
  
  # Solution 6:
  def number(lines):
    x = 1
    for i in range(len(lines)):
        lines[i] = str(x) + ": " + lines[i]
        x+=1
    return lines
    
 
 # Solution 7
 def number(lines):
	return [str(x+1) + ": " + lines[x] for x in range(len(lines))]


# Solution 8
from itertools import starmap

def number(lines):
    return list(starmap("{}: {}".format, enumerate(lines,1)))


# Solution 9
number=lambda l:list(f"{i}: {e}"for i,e in enumerate(l,1))


# Solution 10
def number(lines):
    return list(map(lambda x: '{}: {}'.format(x[0], x[1]), enumerate(lines,1)))
