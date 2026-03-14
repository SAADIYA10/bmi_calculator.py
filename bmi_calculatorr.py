print("BMI calculator")
name = input("enter your name:")
age = int(input("enter your age:"))
weight = float(input("enter your weight:"))
height = float(input("enter your height:"))
bmi = weight/(height**2)
print(" \n hellooo",name)
print("your BMI is:",round(bmi,2))
if bmi<19.5:
    print("you are underweight")
elif bmi>=19.5 and bmi<29.5:
    print("you have normal weight")
elif bmi>=29.5 and bmi<39.5:
    print("you are over weight")
else:
    print("you are obsessed")
