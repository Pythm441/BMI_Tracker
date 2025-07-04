def calculate_bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)

def classify_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def health_tip(Class: str) -> str:
    tips = {
        "Underweight": "Consider a balanced diet with more calories.",
        "Normal weight": "Maintain a balanced diet and regular exercise.",
        "Overweight": "Focus on a healthy diet and increase physical activity.",
        "Obesity": "Consult a healthcare provider for a personalized plan."
    }
    return tips.get(Class, "No specific advice available.")

def save_to_file(name, age, height, weight, bmi, category):
    with open("bmi_records.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Height: {height:.2f} m\n")
        file.write(f"Weight: {weight:.2f} kg\n")
        file.write(f"BMI: {bmi:.2f} ({category})\n")
        file.write("-" * 40 + "\n")
    

def main():
    print("Welcome to the BMI Calculator!")

    name = input("Please enter your name: ").strip().title()
    age = input("Please enter your age: ").strip()

    try:
        weight = float(input("Please enter your weight in kg: ").strip())
        height = float(input("Please enter your height in meters: ").strip())
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")
        return

    print("\nCalculating your BMI...")

    bmi = calculate_bmi(weight, height)
    classification = classify_bmi(bmi)
    tip = health_tip(classification)

    print(f"\n{name}, aged {age}, your BMI is: {bmi:.2f}")
    print(f"Classification: {classification}")
    print(f"Health Tip: {tip}")
    print("\nThank you for using the BMI Calculator!")

    save_to_file(name, age, height, weight, bmi, classification)
    print("Your data has been saved to 'bmi_records.txt'.")

if __name__ == "__main__":
    main()