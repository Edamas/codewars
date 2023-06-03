'''Keep Hydrated!
8 kyu
Python

DESCRIPTION:
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5

TAGs:
  ALGORITHMS
  MATHEMATICS
  FUNDAMENTALS
'''

# Solution 1
def litres(time):
    return time // 2


# Solution 2
def litres(time):
    return int(time * 0.5)


# Solution 3
import math
def litres(time):
    return math.floor(.50 * time)
    

# Solution 4
import math

def litres(time):
    total = time * 0.5
    return math.floor(total)

# Solution 5
def litres(time):
    return int(time * .5)
    

# Solution 6
def litres(time):
	time=int(time)
	litres=0
	for x in range(0,99999):
		if(x != time):
			litres=litres+0.5
		elif(x <= time):
			break
	return int(litres)
  

# Solution 7
litres=lambda t: int(t * 0.5)


# Solution 8
def litres(time):
    return (0.5*time) // 1


# Solution 9
import math

def litres(time):
    return math.trunc(time / 2)


# Solution 10
litres=int(not()).__rlshift__(not()).__int__().__float__().__rfloordiv__


# Bonus Solution:
def litres(time):
    return 'Are you Tom Cruise?' if time < 0 else int(time / 2)
