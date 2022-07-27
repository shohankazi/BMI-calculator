#----------------------BMI Calculator----------------
weight = input("enter your weight (kg): ")
height = input("enter your height (m): ")
BMI = float(weight) / (float(height) * float(height))
print("your BMI ", round(BMI, 2))
if BMI <= 18.5 :
    print("You are underweight ")
elif BMI <= 25 :
    print("you have normal weight")
elif BMI <= 30 :
    print("You are overweight")
elif BMI <= 35 :
    print("you are obese")
elif BMI > 35:
    print("You are clinically obese")

