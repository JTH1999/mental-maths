import random
from config import config, difficulty_options, question_count
import time


def select_option(options):
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    while True:
        try:
            selection = int(input("select: "))
            if selection in range(1, len(options) + 1):
                break
            print("Please enter a valid option")
        except:
            print("Please enter a number associated with one of the difficult options.")
    return options[selection - 1]


print("Please select a game mode")
operator = select_option(list(config.keys()))
print(
    "Please select a difficulty. To select, enter the number associated with the difficulty."
)
difficulty = select_option(difficulty_options).lower()
times = list([time.perf_counter()])
for i in range(0, question_count):
    rand1 = random.randrange(
        config[operator][difficulty]["min"], config[operator][difficulty]["max"]
    )
    rand2 = random.randrange(
        config[operator][difficulty]["min"], config[operator][difficulty]["max"]
    )
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
                times.append(time.perf_counter())
                time_taken = times[i + 1] - times[i]
                print(f"Correct! Time: {time_taken:.3f}")
                loop = False
            else:
                print("Incorrect. Try again.")
        except Exception as e:
            print(e)
            print("Enter valid input you donkey.")

total_time = times[-1] - times[0]
print(f"Congrats! Total time: {total_time:.3f}")
