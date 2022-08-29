from itertools import count


list(range(0,11,2))
print(list)

##
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

#




