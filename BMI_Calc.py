print("Welcome to your BMI Calculator!")

name = input("Please enter your name: ")
age = input("Please enter your age: ")
height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter your weight in kilograms: "))

print("Calculating your BMI...")

bmi = weight / (height ** 2)

print (f"{name}, your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight. you should consider gaining some weight for better health.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight. keep up the good work!")
elif 25 <= bmi < 29.9:
    print("You are overweight. wow , you should consider losing some weight for better health.")
else:
    print("You are obese. god!! you should seriously consider losing weight for better health.")


print("Health tip: Continue eating a balanced diet and exercising regularly to maintain a healthy weight.")
print("Thank you for using the BMI Calculator. Goodbye!")