'''
They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story
#1: Are they opposite?
8 kyu
Python


Task

Give you two strings: s1 and s2. If they are opposite, return true; otherwise, return false. Note: The result should be a boolean value, instead of a string.

The opposite means: All letters of the two strings are the same, but the case is opposite. you can assume that the string only contains letters or it's a empty string. Also take note of the edge case - if both strings are empty then you should return false/False.


Examples (input -> output)

"ab","AB"     -> true
"aB","Ab"     -> true
"aBcd","AbCD" -> true
"AB","Ab"     -> false
"",""         -> false


TAGs:
  PUZZLES
  GAMES
'''


# Solution 1
def is_opposite(s1,s2):
    case_s1 = [char.isupper() for char in s1]
    case_s2 = [char.islower() for char in s2]
    return s1 != '' and case_s1 == case_s2
    

# Solution 2
def is_opposite(s1, s2):
    return False if not(s1 or s2) else s1.swapcase() == s2
  

# Solution 3
def is_opposite(s1,s2):
    return s1 != "" and s1.swapcase() == s2

# Solution 4
def is_opposite(s1,s2):
  if s1.swapcase() == s2 and s1 != "":
    return True
  else:
    return False
  

# Solution 5
def is_opposite(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return False
    for i in range(len(s1)):
        if s1[i].swapcase() == s2[i]:
            return True
        else:
            return False
          

# Solution 6
def is_opposite(s1,s2):
    return all([s1, s2, s1 == s2.swapcase()])
  

# Solution 7
def is_opposite(s1,s2):
  return s2 == ''.join(i.lower() if i.isupper() else i.upper() for i in s1) and s1 != ""


# Solution 8
def is_opposite(s1,s2):
    return s1.swapcase() == (s2 or False)
  

# Solution 9
is_opposite=lambda a,b:False if not a else a.swapcase()==b


# Solution 10
def is_opposite(s1,s2):
  return sum([abs(ord(s1[i])-ord(s2[i]))!=32 for i in range(len(s1))])==0 if (s1 and s2) else False
