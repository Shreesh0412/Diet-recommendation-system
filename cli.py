from dietlogic import calories,diet
from utils import userinput,output,warning

def main():
    goal,age,weight = userinput()
    calories1 = calories(weight, goal)
    diet1 = diet(goal)
    output(calories1, diet1)
    warning()

while True:
    main()
    a=print("Do you wish to continue? (y/n)")
    if a==n:
        break
