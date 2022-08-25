
str1 = "Welcome to Berlin"
print("The length of the string  is :", len(str1))


# check if an number is an even number of odd number

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

    #  Write a program that detects if a string has an even/odd number of characters and prints even or "odd" ? Using input/ output
  #Input  Output

#"hello world"        "odd"  
#"hello planet"       "even"  
                
a = int(input("Enter the number to find odd or even "))
if (a % 2) == 0:
    print("{0} is Even".format(a))
else:
    print("{0} is Odd".format(a))

