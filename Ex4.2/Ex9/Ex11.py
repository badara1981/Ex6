# Python3 program to demonstrate the 
# use of replace() method  
  
string = "geeks for geeks geeks geeks geeks" 
   
# Prints the string by replacing all
# geeks by Geeks 
print(string.replace("geeks", "Geeks")) 
  
# Prints the string by replacing only
# 3 occurrence of Geeks  
print(string.replace("geeks", "GeeksforGeeks", 3))

# Ex
animal_pets = """A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."""
print(f'{animal_pets.replace("dog","cat")}')