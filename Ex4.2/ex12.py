
list(range(0,11,2))
print(list)

## formating
index_count = 0
for letter in 'abcde':
    print('At index{} the  letter is {}'.format(index_count,letter))
index_count += 1


#
index_count = 0
word = "abcde"
for letter in word:
    print(word[index_count])
    index_count += 1
print(index_count)
#  two bold function

word = "abcd"
for item in enumerate(word):
    print(item)
    #
    word ="abcd"
    
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')


#Zip function in python

myList1 = [1,2,3]
myList2  = ['a','b','c']
myList3 = [100, 200, 300]

for item in zip(myList1, myList2,myList3):
    for a,b,c in zip(myList1,myList2,myList3):
        print(a)
    print(item)
    list(zip(myList1,myList2))
#
    'x' in ['x','y','z']
    print('x')