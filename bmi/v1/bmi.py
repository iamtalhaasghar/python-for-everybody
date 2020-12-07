# Body Mass Index Calculator Script
# Version 1
# Talha Asghar
# 30 Nov 2020

name = input("Enter your name: ")
mass = int(input("Enter your mass (in kg): "))
height = int(input("Enter your height (in cms): "))

height = height / 100 # converting height from centimeters into meters

bmi = mass / (height ** 2) # formula to calculate bmi

print("Hey, " + name + " your BMI is: " + str(bmi))

