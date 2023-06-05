'''
Convert boolean values to strings 'Yes' or 'No'.
8 kyu
Python

Instructions:
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.


TAGs:
  FUNDAMENTALS
'''


# Solution 1
def bool_to_word(boolean):
    return "Yes" if boolean else "No"
  

# Solution 2
def bool_to_word(bool):
    if bool:
        return 'Yes'
    else:
        return 'No'
      

# Solution 3
def bool_to_word(bool):
     if bool:
         return "Yes"
     return "No"
  

# Solution 4
def bool_to_word(boolean):
    return ['No', 'Yes'][boolean]
  

# Solution 5
bool_to_word = {True: 'Yes', False: 'No'}.get


# Solution 6
bool_to_word = lambda b: b and "Yes" or "No"


# Solution 7
bool_to_word= lambda _:{1:'Yes'}.get(_,'No')


# Solution 8
bool_to_word=lambda b:"YNeos"[1-b::2]


# Solution 9
bool_to_word = lambda b : ["No", "Yes"][b];


# Solution 10
bool_str = {
    True: 'Yes',
    False: 'No'
}

def bool_to_word(boolean):
    return bool_str[boolean]
