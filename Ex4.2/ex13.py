
from random import shuffle 
list  = [ 10, 20, 30, 40, 100]
print(min(list))

print(max(list))

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(myList)

#
print("Today is  my Birthday party")
print('Am going to the beach')
print("we are going to Rio Jeneiro 'We are in Brazil'")
print('We are now on my trip to Berlin')
print("hello" +  " world")
greeting = "Hello"
name = input("write name of someone here: ")
print(greeting+  ' ' +name)
name = input("Please enter your name")
print(greeting + ' ' + name) 

#  The Escape  Character  in String  using 
# Backlash
# Here we using SPLIT OPERATOR to break the string into various 

splitString = "This string has been! \nsplit over \nseveral  \nlines"
print(splitString)

tabbedString = "1\t2, \t3, \t4,\t5"
print(tabbedString)
print('The shop owner say"No, no,    \'e\'t \'b resting".')
print("The shop owner say \"Yes , yes, 's' uuh,...This is the end....")
print("""THe  shop owner say no"then we have to do something" """)

# Another Split String

anotherSplitString = """ This is the string
 split over
 several
  line
"""
print(anotherSplitString)

#  another SplitString  \
   
anotherSplitString = """ This is the string
 split over \
 several \
  line \
"""
print(anotherSplitString)

# variables  and types
name = "Badara"
greeting = "Hello"
print(greeting + name)
age = 24
print(age)

print(type(greeting))
print(type(age))
age = "2 year"
print(age)
print(type(age))

# Numeric Data types in   python

# numeric
# iterate
# sequence ( which are also iterate)
 #  mapping
 # file
 # class
 # exception

 # python3 has three numeric data type
 #int 
 # float 
 #  complex

# python  integer data are called int
# integer are called whole number they have no fractional part/ numbers or remainder
# float is  called real number  number having fractional part after the decimal point 

a =  12
b = 3
print(a + b) # 15
print(a - b) # 9
print(a * b)  # 36
print(a / b) # 4.0
print(a // b) # 4 integer division round down towards minus  infinity
print(a % b) # 0 modulo: the reminder after integer  divisions


#  sample of int

for i in  range(1, 4):
    print(i)

    for i in range(1, a//b):
        print(i)

## OPeration precedences

print(a + b / 3 -  4  * 12)
print(a +  (b / 3) - (4 * 12))
print(a + (b * 89) -(5 * 44))
print((((a +b) / 3) - 4 ) * 12)

c = a + b
d = c / 3
e  = d - 4
print(e  * 12)
