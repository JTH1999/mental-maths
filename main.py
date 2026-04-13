import random
import operator
operators = ["+", "-", "*", "/"]
config = {
        "+": {
                "operator": operator.add,
                "max": 9999,
                "min": 1000,
            },
        "-": {
                "operator": operator.sub,
                "max": 9999,
                "min": 1000,
            },
        "*": {
                "operator": operator.mul,
                "max": 99,
                "min": 10,
            },
        "/": {
                "operator": operator.truediv,
                "max": 99,
                "min": 10,
            },
        }
for operator in operators:
    rand1 = random.randrange(config[operator]["min"], config[operator]["max"])
    rand2 = random.randrange(config[operator]["min"], config[operator]["max"])
    if operator == "/":
        ans = rand1
        equation = f"{rand1 * rand2} {operator} {rand2}"
    else:
        ans = config[operator]["operator"](rand1, rand2)
        equation = f"{rand1} {operator} {rand2}"

    print(f"Equation: {equation}")

    loop = True
    while loop:
        try:
            ans_input = input("Answer: ").strip()
            user_ans = int(ans_input)
            if user_ans == ans:
                print("Correct! Well done dipshit.")

                loop = False
            else:
                print("Incorrect. You were able to do this when you were 6. Try again.")
        except:
            print("Enter valid input you donkey.")
