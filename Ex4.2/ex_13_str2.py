# 0123456789101234

from cgi import print_environ


parrot = "Norwegian parrot"
print(parrot)
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

# Negative indexing in string

print(parrot[-11])
print(parrot[-10])
print(parrot[-11])
print(parrot[-9])
print(parrot[-8])
print(parrot[-6])

 # minus negative in string
print(parrot[3-14])
print(parrot[4-14])
print(parrot[8-14])
print(parrot[6-14])
print(parrot[3-14])
print(parrot[5-14])

# Let talk  look at concept of  SLICING 

parrot = "Norwegian  Blue"

print(parrot[0:6]) # Norweg   Note in slicing you have to know that the last number for example 6 is always exclude from count
print(parrot[1:8]) # 
print(parrot[2:8])
print(parrot[3:8])
print(parrot[4:8])
print(parrot[:9])
print(parrot[10:14])
print(parrot[10:])
print(parrot[11:])
print(parrot[6:])
print(parrot[:6])
print(parrot[:6]  + parrot[6:0])
print(parrot[:])


# string formatting  cubic

for i in range (1, 13):
    print("No. {0:2} squared is {1:4} and cube is{2:4}".format(i, i ** 2, i **3))
    
    #inputs
    input = ("Enter a number here")