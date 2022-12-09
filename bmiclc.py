# hello to this code
# It's written in python
# Reza Moghaddas

# Color
class color :
    green = '\033[92m'
    yellow = '\033[33m'
    white = '\033[37m'
    red = '\033[31m'

# Data Entry

print(color.yellow +"Welcome! Please answer this questions to calculate your BMI")
# gender = (input("Are you male or female ? (m/f) : "))
# print(color.white + '')
qad = float(input(color.white +"Enter your height in Centimeter : "))
vazn = float(input("Enter your weight in Kilogram : "))

# Processing
# p_1 convert cm to m /100
qad_m = qad/100
# calc bmi -- bmi is vazn/qad**
BMI = vazn/(qad_m**2)
print(color.yellow + "your BMI is : ")
print(BMI)

print("-_-_-_-_-_-_-_-_-_-_-_-_")

if BMI < 18.5 :
    print(color.red + "Weight deficiency") # kambood vazn
elif BMI < 24.5 :
    print(color.green + "congratulation! you are healthy") # salem
elif BMI < 30 :
    print(color.red + "you are overweight") # ezafe vazn
elif BMI >= 30:
    print(color.red+'You are Severe obesity!!!') # chaq

print(color.yellow + "-_-_-_-_-_-_-_-_-_-_-_-_")
print(color.white + "thanks 4 using me , written by \"Reza Moghaddas\"")
