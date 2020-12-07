# Body Mass Index Calculator
# Version 2

name = input("Enter your name: ")
mass = input("Enter your weight (in kgs): ")
mass = int(mass)

height = input("Enter your height (in cms): ")
height = int(height)
height = height / 100

bmi = mass / (height ** 2) # formula to calculate bmi

# BMI Categories:
# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater


category = ''

if bmi < 18.5:
    category = 'Underweight'
elif bmi >= 18.5 and bmi <= 24.9:
    category = 'Normal'
elif bmi >= 25 and bmi <= 29.9:
    category = 'Overweight'
else:
    category = 'Obesse'

print("Your bmi is %.2f and your Category is: %s" % (bmi, category))