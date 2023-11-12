import random


def generate_random_integer(minimumNum, maximumNum):
    """
    Generate a random integer between minimum and maximum.
    """
    return random.randint(minimumNum, maximumNum)


def generate_random_operator():
    """
    Generate a random mathematical operator: '+', '-', or '*'
    """
    return random.choice(['+', '-', '*'])


def calculate_result(num1, num2, operator):
    """
    Calculate the result of the mathematical expression.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return problem, result


def math_quiz():
    """
    Conduct a math quiz game with three questions and provide feedback on the user's answers.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, correct_answer = calculate_result(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_answer = 0

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()

