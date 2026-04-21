#String operations in python

#string manipulation
text="Python is fun"
print("Upper : ",text.upper())
print("Lower : ",text.lower())

#concatination and repetation
a="Hello "
b="World"
print(a+b)
print(a*10)

#string methods
name="ashok"
print(name.capitalize()) #Ashok
print(name.find("a")) # gives index of a(0)
print(name.replace("a","@"))

#lenght of string
text="Python"
print(len(text)) #6

#Accessing characters
text="Pyton"
print(text[0])
print(text[-1])

#string slicing
text="String slicing"
print(text[:6])
print(text[7:])
print(text[::2])

#Escape sequence
print("Learning\nPython")
print("Learning\tPython")