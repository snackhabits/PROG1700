"""
Variables and Comments

Program: PROG1700; variables and comments
Author: Joey MacDonald
Last Date Modified: 21/09/22
Purpose of this program is to demonstrate knowledge and usage of strings
"""
NAME = "Duncan James Joseph MacDonald"
NAMESHORT = "Joey"
age = int(31) #my current age
GENDER = "Male" #my gender
BIRTHYEAR = int(1991) #my year of birth
HOMETOWN = "Port Hastings" #hometown i grew up in
SCHOOL = "SAERC" #highschool I attended
sportA = "Football" #sport i played the most growing up
sportAposition = "Offensive Lineman"
sportB = "Hockey" #sport I enjoy watching the most
HEIGHT = float(180.3) #my height in cm
weight = float(225.4) #my weight in pounds
hairC = "brown hair" #the color of my hair
hairL = "short-ish" #the length of my hair
UNI = "Memorial University of NewfoundLand" #University i attended
COLLEGE = "NSCC Strait Area Campus" #college i attended
career_one = "Power Engineer" #career I spent 5 years working in
'''
End of StoryTime part I
'''
txtone="Hello, My name is {}, but I go by {}.\nI'm {} as I was born in {} and grew up in {}"  #text string for basic personal info
txttwo="Went to Highschool at {} where I played {} as a {}, after which I coached {}" #text string for school and sports
txtpersonal= "I'm a {} with {} {} and am {} cm tall and weight {} lbs" #text string for physical attributes
txtpostsec= "After HS I attended {} before leaving and attending\n{} for {} where I worked for five years." #text string for post secondary education/training
print(txtone.format(NAME, NAMESHORT, age, BIRTHYEAR, HOMETOWN))
print(txttwo.format(SCHOOL, sportA, sportAposition, sportB))
print(txtpersonal.format(GENDER, hairL, hairC, HEIGHT, weight))
print(txtpostsec.format(UNI, COLLEGE, career_one))
'''
End of StoryTime part II


'''