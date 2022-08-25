#
myList = [ 1, 2,3, 4, 5,6]
for num in myList:
    print(num)

    #for Example 2

myList = [ 1, 2,3, 4, 5,6, 7,8, 9, 10]
for jelly in myList:
    print(jelly)
    print("Hello")

 #ex.2

# check for Even
 # Odd Number
for num in myList:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')

list_sum = 0
for num in myList:
    list_sum = list_sum + num
    print(list_sum)

for n in range(1,101):
    if( n % 3 == 0 and  n % 5 == 0):
        print("Fizz Buzz")
if( n % 3 == 0):
        print("Fizz")
elif( n % 5 == 0 ):  
        print("Buzz")
else:
    print(n)

#string
mystring = "Hello World!"
for letter in mystring:
    print(letter)

# string example 2
    myCountry = "The   Gambia"
    for city in myCountry:
        print(city)

# numbers
tup = (1, 2, 3, 4, 5, 6)
for item in tup:
  print(item)
  
  #

  #  two ball pairs

  list = [ (1,2), (3,4), (5,6), (7,8) ]
  len(list)
  
  #  Example

  for items in list:
    print(items)
    #
    myList = [(1,2,5), (5,8,4),( 5,4,6)]
    for a, b, c in myList:
        print(a,b,c)
        print(a)
        print(b)
        print(c)

#Dictionary in loops
#Example one  you can use 2 burn package in Dictionary as well to iterate the loop

d = {'k1':1,'k2':2, 'k3':3, 'k4':4 }
for items in d.items():
    print(items)

#Example 2

d = {'k1':1,'k2':2, 'k3':3, 'k4':4 }
for key,value in d.items():
    print(key)
    #print(value)

    #
    d = {'k1':1,'k2':2, 'k3':3, 'k4':4 }
    for value in d.values():
        print(value)
    
    #WHILE LOOPS

    x = 0
    while x < 5:
        print(f'the current value of x is {x}')
        x += 1
    else:
            print("X IS NOT LESS THAN 5")
            
            
            # USING PASS
            list_item = [ 2, 5, 8]
            for list_item in list_item:
             pass
            print("my string in path")

            # let start using the string as well 
            mystring = "sammy"
            for letter in mystring:
                print(letter)
                #
                for letter in mystring:
                    if letter == "a":
                        continue
                    print(letter)
                #  Ex 
    ##x = 0
    #while  x < 5:
     
     #if x == 2:
        #break  
        
        
        #print(x)
        
        # x += 1
#  example of using Ranges

#list = [1, 2, 3 ]
#for num in range(3,10):
    #print(num)
#Ex
list = [ 1, 2, 3]
for num in range(0, 11, 2):
    print(num)
#
x = "Mary"
print(x[1])
print(x[0:2])
print(x[:3])
print(x[1:2])
print(x[1:])
print(x[2:])

#  Create a Variable called City and print the name London on the screen

city = "London"
print(city)
#
city = "London"
#
city = input("Enter name of the city")
print("You entered the word "  + city)

# ex2





