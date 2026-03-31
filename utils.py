def userinput():
    print("Diet Recommendation System")
    goal = input("Enter goal (loss/gain/maintenance): ").lower()
    age = int(input("Enter age: "))
    weight = float(input("Enter weight(kg): "))
    return goal, age, weight

def output(calories, diet):
    print("\n Your Diet Plan")
    print(f"Recommended Calories:{int(calories)} kcal\n")
    for meal, item in diet.items():
        print(f"{meal}:{item}")

def warning():
    junk = input("\nDo you eat junk food frequently? (yes/no): ").lower()
    if junk == "yes":
        print("Warning: Reduce junk food for a healthier lifestyle!")
    elif junk == "no":
        print("Very Good, Keep it going")
    else:
        print("Invalid input")
