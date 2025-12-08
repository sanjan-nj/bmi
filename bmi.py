def get_user_input():
    """Collects and validates user input."""
    while True:
        try:
            age = int(input("Enter your age: "))
            height = float(input("Enter your height in meters (e.g., 1.75): "))
            weight = float(input("Enter your weight in kg: "))

            if age <= 0 or height <= 0 or weight <= 0:
                print("Values must be greater than 0. Try again.\n")
                continue

            return age, height, weight
        except ValueError:
            print("Invalid input! Please enter numbers only.\n")


def calculate_bmi(height, weight):
    """Returns BMI value."""
    return weight / (height ** 2)


def get_bmi_category(bmi):
    """Returns BMI category name."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Fit / Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


def get_advice(category):
    """Returns what to do and what not to do based on category."""
    advice = {
        "Underweight": {
            "do": [
                "Eat calorie-dense food like bananas, nuts, ghee, milk.",
                "Exercise lightly to build muscle.",
                "Increase protein intake."
            ],
            "dont": [
                "Skipping meals.",
                "Excessive cardio."
            ]
        },
        "Fit / Normal": {
            "do": [
                "Maintain a balanced diet.",
                "Exercise regularly.",
                "Get proper sleep."
            ],
            "dont": [
                "Eating junk frequently.",
                "Irregular sleep schedule."
            ]
        },
        "Overweight": {
            "do": [
                "Reduce sugar and oily foods.",
                "Walk/jog 30 minutes daily.",
                "Control portion sizes."
            ],
            "dont": [
                "Eating heavy at night.",
                "Drinking sugary beverages."
            ]
        },
        "Obese": {
            "do": [
                "Follow a controlled diet plan.",
                "Consult a fitness trainer/doctor.",
                "Increase daily physical activity."
            ],
            "dont": [
                "Skipping exercise.",
                "Eating fast food frequently."
            ]
        }
    }

    return advice[category]


def display_results(bmi, category, advice):
    """Displays the final result."""
    print("\n---- BMI RESULT ----")
    print(f"BMI Value   : {bmi:.2f}")
    print(f"Category    : {category}")
    print("\nWhat you should do:")
    for item in advice["do"]:
        print("- " + item)

    print("\nWhat you should NOT do:")
    for item in advice["dont"]:
        print("- " + item)


def bmi_calculator():
    print("---- BMI CALCULATOR ----")

    age, height, weight = get_user_input()
    bmi = calculate_bmi(height, weight)
    category = get_bmi_category(bmi)
    advice = get_advice(category)

    display_results(bmi, category, advice)


# Run the program
bmi_calculator()