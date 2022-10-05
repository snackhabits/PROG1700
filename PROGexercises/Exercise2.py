""""
Numeric Types Exercise
Program: PROG1700; variables and comments
Author: Joey MacDonald
Last Date Modified: 21/09/22
Purpose of this program is to demonstrate the basic usages of numbers
"""
num_x = int(37)
num_y = int(8)
num_r = float(4.1)
num_s = float(11.4)
print(num_x + num_y) 
print(num_r + num_s)
print(num_x * num_r)
num_1 = int(2)
num_2 = int(10)
print(num_1%num_2) #result of 2 is whats left when dividing 2 by 10
print(num_2%num_1) #result of 0 is whats left when dividing 10 by 2
print(num_1-num_2)
print(num_1*num_2)
print(num_2/num_1)
print(num_2**num_1)
print(num_2//num_1)
x=37
y=8
z=5
x+=3 #equivilent to x = x + 3 ; x=37+3=40
x-=5 #equivelent to x = x - 5 ; x=40-5=35
y*=2 #equivelent to y = y * 2 ; y=8*2=16
y/=2 #equivelent to y = y / 2 ; y=16/2=8
Z = y%z; #equivelent to Z = Z % 5 ; Z=100%5=0
z**=3 #equivelent to z = z ** 3 ; z=5**3=125
print(z)
print(Z)