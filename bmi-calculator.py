#!/usr/bin/python3
print(">>>THIS PROGRAM COMPUTES THE BODY MASS INDEX (BMI) OF PATIENTS<<<")
foot = float(input("Enter your Height in foot: "))
weight = float(input("Enter your Weight in kg: "))
height_inches = foot * 12
height_centimeters = height_inches * 2.54
height_meters = height_centimeters / 100
BMI = weight / (height_meters * height_meters)
print("your height in inches is: {}".format(height_inches))
print("your height in centimeters is: {}".format(height_centimeters))
print("your height in meters is: {}".format(height_meters))
print("your Body Mass Index (BMI) is: {}".format(BMI))
if BMI > 0:
    if BMI <= 16:
        print("RESULT >>> YOU ARE SEVERELY UNDERWEIGHT! <<<")
    elif BMI <= 18.5:
        print("RESULT >>> YOU ARE UNDERWEIGHT! <<<")
    elif BMI <= 25:
        print("RESULT >>> YOU ARE HEALTHY! <<<")
    elif BMI <= 30:
        print("RESULT >>> YOU ARE OVERWEIGHT! <<<")
    else:
        print("RESULT >>> YOU ARE SEVERELY OVERWEIGHT! <<<")
else:
    print(">>> Enter valid details <<<")
