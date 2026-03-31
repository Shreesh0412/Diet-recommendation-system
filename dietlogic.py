def calories(weight, goal):
    if goal == "loss":
        g=weight*25
        return g
    elif goal == "gain":
        g=weight*35
        return g
    else:
        g=weight*30
        return g


def diet(goal):
    if goal == "loss":
        return {
            "Breakfast": "Oats + Fruits",
            "Lunch": "Brown rice + Dal + Vegetables",
            "Dinner": "2 Chapati + Sabzi",
            "Snacks": "Nuts / Green Tea"
        }

    elif goal == "gain":
        return {
            "Breakfast": "Milk + Banana + Peanut Butter",
            "Lunch": "Rice + Paneer / Chicken",
            "Dinner": "Chapati + Eggs/Paneer",
            "Snacks": "Dry fruits + Smoothie"
        }

    else:
        return {
            "Breakfast": "Poha / Upma + Fruits",
            "Lunch": "Rice + Dal + Vegetables",
            "Dinner": "Chapati + Sabzi",
            "Snacks": "Fruits / Nuts"
        }
