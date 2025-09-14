import math
def create():
    Name=input("Enter your name: ")
    Age=int(input("Enter your age: "))
    Height=float(input("Enter your height in meters: "))
    Weight=float(input("Enter your weight in kilograms: "))
    BMI=Weight/(Height**2)
    print(f"Hello {Name}, you are {Age} years old, {Height} meters tall, and weigh {Weight} kg.")
    print(f"Your Body Mass Index (BMI) is: {BMI:.2f}")
create()
