
#Indentation would be a good process here we have to always try to Indent our code
# long name is not also defined therefore we have to use short and reasonable names

#  wrong code 
#bar = long_function_name(num_one, num_two,
    #num_three, num_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    num_one, num_two, num_three,
    num_four):
    print(num_one)

    

# Correct:

# Aligned with opening delimiter.
#bar = long_function_name(num_one, num_two,
     #                    num_three, num_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        num_one, num_two, num_three,
        num_four):
    print(num_one)

# Hanging indents should add a level.
#bar = long_function_name(
   # num_one, num_two,
    #num_three, num_four)
    
    #  Maximum Line Length
#For flowing long blocks of text with fewer structural restrictions (docstrings or comments), the line length should be limited to 72 characters.fewer structural restrictions (docstrings or comments), the line length should be limited to 72 characters.

#Source File Encoding

#Code in the core Python distribution should always use UTF-8, and should not have an encoding declaration.

#In the standard library, non-UTF-8 encodings should be used only for test purposes. Use non-ASCII characters sparingly, preferably only to denote places and human names. If using non-ASCII characters as data, avoid noisy Unicode characters like z̯̯͡a̧͎̺l̡͓̫g̹̲o̡̼̘ and byte order marks
#All identifiers in the Python standard library MUST use ASCII-only identifiers, and SHOULD use English words wherever feasible (in many cases, abbreviations and technical terms are used which aren’t English).

#Open source projects with a global audience are encouraged to adopt a similar policy.

#Imports

#Imports should usually be on separate lines:
# Correct:
import math
import os
# Wrong:
import math, os
#It’s okay to say this though:Imports
#Imports should usually be on separate lines:

# Correct:
import os
import sys

# Wrong:
import sys, os
#It’s okay to say this though:Imports
#Imports should usually be on separate lines:

# Correct:
import sys
import os

# Wrong:
import math, os
#It’s okay to say this though:

# Correct:
from subprocess import Popen, PIPE

#Whitespace in Expressions and Statements 
#Pet Peeves
#Avoid extraneous whitespace in the following situations:

# Wrong:
#spam( ham[ 1 ], { eggs: 2 } )


# Correct:
#spam(ham[1], {eggs: 2})


#Between a trailing comma and a following close parenthesis:
# Correct:
foo = (0,)
# Wrong:
bar = (0, )
#Immediately before a comma, semicolon, or colon:
 
 #Correct:
spam(ham[1], {eggs: 2})

# Wrong:
spam( ham[ 1 ], { eggs: 2 } )

#Between a trailing comma and a following close parenthesis:

# Correct:
foo = (0,)

# Wrong:
bar = (0, )
#Immediately before a comma, semicolon, or colon:
# Correct:
if x == 4: print(x, y); x, y = y, x
# Wrong:
if x == 4 : print(x , y) ; x , y = y , x