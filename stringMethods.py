a = """My
name
is 
XoXo."""
b = '''I 
study
in
ISL Engineering College.'''
print(a) 
print(b) 
print(a+b)
a = "Hello, World! "
print(a*2) #returns “Hello, World! Hello, World!”
print(a[1]) #Get the character at position 1 
print(a[2:5]) #Substring. Get the characters from position 2 to position 5 (not included)
print(a.strip()) # returns "Hello, World!" 
print(len(a))
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']