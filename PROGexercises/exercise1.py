"""
Variables and Comments

Program: PROG1700; variables and comments
Author: Joey MacDonald
Last Date Modified: 21/09/22
Purpose of this program is to demonstrate the basic usages of variables and comments
"""
NAME = "Duncan James Joseph MacDonald"
nameshort = "Joey"
age = int(31) #my current age
gender = "Male" #my gender
birthyear = int(1991) #my year of birth
hometown = "Port Hastings" #hometown i grew up in
school = "SAERC" #highschool I attended
sportA = "Football" #sport i played the most growing up
sportAposition = "Offensive Lineman"
sportB = "Hockey" #sport I enjoy watching the most
height = float(180.3) #my height in cm
weight = float(225.4) #my weight in pounds
hairC = "brown hair" #the color of my hair
hairL = "short-ish" #the length of my hair
university = "Memorial University of NewfoundLand" #University i attended
college = "NSCC Strait Area Campus" #college i attended
career = "Power Engineer" #career I spent 5 years working in
'''
End of StoryTime part I
'''
txtone="Hello, My name is {},but i go by {}. I'm {} as i was born in {} and grew up in {}"  #text string for basic personal info
txttwo="Went to Highschool at {} where i played {} as a {}, after which I coached {}" #text string for school and sports
txtpersonal= "I'm a {} with {} {} and am {} cm tall and weight {} lbs" #text string for physical attributes
txtpostsec= "After HS I attended {} before leaving and attending \n {} for {} where i worked for five years." #text string for post secondary education/training
print(txtone.format(NAME, nameshort, age, birthyear, hometown))
print(txttwo.format(school, sportA, sportAposition, sportB))
print(txtpersonal.format(gender, hairL, hairC, height, weight))
print(txtpostsec.format(university, college, career))
'''
End of Story Time Part II
'''
