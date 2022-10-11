""""
Numeric Types Exercise
Program: PROG1700; String functions
Author: Joey MacDonald
Last Date Modified: 21/09/22
Purpose of this program is to demonstrate the basic usage of string functions
"""

name = "duncan"         
x = name.capitalize()           #capitalizes first letter in string
print(x)

sports = "FoOtBaLl"
x_one = sports.lower()             #converts string to lowercase lettering
print(x_one)

txtone = "I enjoy eating apples and oranges"
y = txtone.replace("apples and oranges", "candy")           #replaces first text string with new string
print(y)

stringthing = "September is a terrible month"
z = stringthing.startswith("September")             #If string starts with chosen string, returns TRUE
print(z)

r = stringthing.title()                 #Converts first character to upper case lettering
print(r)

s = stringthing.upper()              #converts string to uppercase lettering
print(s)
