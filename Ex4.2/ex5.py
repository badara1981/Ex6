
def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('Barcelona'))
print(string_both_ends('333'))
print(string_both_ends('000'))

#  

str1 = "Python"
str2 = "is a popular scripting language"

# Combine the string values using '%' operator
print("The output after combining strings:\n\n%s %s" % (str1, str2))

## Python 3.4 endswith()
def make_3sg_form():
    Word = input('Enter a word: ')
    if Word.endswith('Shrink'):
        New_word=Word[:+4]+'inator 6000'
        print(New_word)
    if Word.endswith(('o', 'ch', 's', 'sh', 'x' or 'z')):
        New_word=Word[:+4]+'Doom'
        print(New_word)
    if Word !=Word.endswith((('o', 'ch', 'y', 's', 'sh', 'x' or 'z'))):
        New_word=Word[:+10]+'inator 4000'
        print(New_word)
        if Word.endswith("EvilClone"):
            New_word=Word[:+4]+"inator 9000"
            print(New_word)
make_3sg_form()
# solution 2

def make_3sg_form():
    Word = input('Enter a word: ')
    if Word.endswith('h'):
        New_word=Word[:-1]+'ies'

    elif Word.endswith(('o', 'ch', 's', 'sh', 'x' ,'z' 'eh')):
        New_word=Word+'ies'

    else:
        New_word=Word+'s'
    print(New_word)
make_3sg_form()
