userInput = input("something to be converts: ")
u_or_l = input("u for upper case and l for lower case  ")
if u_or_l.lower() == 'u':
    f =userInput.upper()
    print(f)
elif u_or_l.lower() == 'i':
    f = userInput.lower()
    print(f)
else:
    print("print something else")

#Example
x = input("Put something here")
if(x.isupper()):
    print(x.lower())
    if(x.lower()):
        print(x.upper())