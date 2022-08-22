
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
