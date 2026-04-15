import operator

difficulty_options = ["Easy", "Medium", "Hard"]
question_count = 3
config = {
    "+": {
        "operator": operator.add,
        "name": "Addition",
        "easy": {
            "max": 999,
            "min": 10,
            "operand_count": 2,
            "time": {"bronze": 10, "silver": 6, "gold": 3},
        },
        "medium": {
            "max": 9999,
            "min": 100,
            "operand_count": 2,
            "time": {"bronze": 10, "silver": 6, "gold": 3},
        },
        "hard": {
            "max": 99999,
            "min": 10000,
            "operand_count": 3,
            "time": {"bronze": 10, "silver": 6, "gold": 3},
        },
    },
    "-": {
        "operator": operator.sub,
        "name": "Subtraction",
        "easy": {
            "max": 999,
            "min": 10,
            "operand_count": 2,
            "time": {"bronze": 10, "silver": 6, "gold": 3},
        },
        "medium": {
            "max": 9999,
            "min": 100,
            "operand_count": 2,
            "time": {"bronze": 10, "silver": 6, "gold": 3},
        },
        "hard": {
            "max": 99999,
            "min": 10000,
            "operand_count": 3,
            "time": {"bronze": 10, "silver": 6, "gold": 3},
        },
    },
    "*": {
        "operator": operator.mul,
        "name": "Multiplication",
        "easy": {
            "max": 99,
            "min": 1,
            "operand_count": 2,
            "time": {"bronze": 10, "silver": 6, "gold": 3},
        },
        "medium": {
            "max": 99,
            "min": 10,
            "operand_count": 2,
            "time": {"bronze": 10, "silver": 6, "gold": 3},
        },
        "hard": {
            "max": 999,
            "min": 100,
            "operand_count": 2,
            "time": {"bronze": 10, "silver": 6, "gold": 3},
        },
    },
    "/": {
        "operator": operator.truediv,
        "name": "Division",
        "easy": {
            "max": 99,
            "min": 1,
            "operand_count": 2,
            "time": {"bronze": 10, "silver": 6, "gold": 3},
        },
        "medium": {
            "max": 99,
            "min": 10,
            "operand_count": 2,
            "time": {"bronze": 10, "silver": 6, "gold": 3},
        },
        "hard": {
            "max": 999,
            "min": 100,
            "operand_count": 2,
            "time": {"bronze": 10, "silver": 6, "gold": 3},
        },
    },
}
