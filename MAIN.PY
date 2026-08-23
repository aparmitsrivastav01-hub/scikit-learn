print("Your BMI calculator")

W = float(input("Enter your weight (in kilograms) = "))
H = float(input("Enter your height (in metres) = "))

x = W / (H * H)

print("So your BMI would be:", x,)

if x <= 18.5:
    print("You are in Underweight category")

elif x <= 24.9:
    print("You are in Normal category")

elif x <= 29.9:
    print("You are in Overweight category")

elif x <= 34.9:
    print("You are in Obese category")

else:
    print("You are in Extremely Obese category")