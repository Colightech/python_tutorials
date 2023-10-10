#!/usr/bin/python3
print("THIS PROGRAM COMPUTES THE BODY MASS INDEX (BMI)")
Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your weight in kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("your Body Mass Index is: ", BMI)
if BMI > 0:
    if BMI <= 16:
        print("Result >>>are severely underweight<<<")
    elif BMI <= 18.5:
        print("Result >>>you are underweight<<<")
    elif BMI <= 25:
        print("Result >>>you are healthy<<<")
    elif BMI <= 30:
        print("Result >>>you are overweight<<<")
    else: print("Result >>>you are severely overweight<<<")
else: (">>>Enter valid details<<<")
