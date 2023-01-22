import random


def generate_problem(difficulty, operations, range_of_numbers):
    if difficulty == 1:
        operation = random.choice(operations[:2])
    elif difficulty == 2:
        operation = random.choice(operations[:4])
    else:
        operation = random.choice(operations)
    num1 = random.randint(1, range_of_numbers)
    num2 = random.randint(1, range_of_numbers)
    if operation == '**':
        question = str(num1) + ' ** ' + str(num2)
        answer = num1 ** num2
    else:
        question = str(num1) + ' ' + operation + ' ' + str(num2)
        answer = eval(question)
    return question, answer


def check_answer(question, correct_answer, user_answer):
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print('Incorrect. The correct answer is', correct_answer)
        return False


def calculate_score(correct, total):
    score = correct / total
    if score < 0.6:
        return 2
    elif score >= 0.6 and score < 0.75:
        return 3
    elif score >= 0.75 and score < 0.9:
        return 4
    else:
        return 5


def math_test(difficulty, operations, range_of_numbers, total_problems):
    correct = 0
    for i in range(total_problems):
        question, answer = generate_problem(difficulty, operations, range_of_numbers)
        print(question)
        user_answer = float(input('Enter your answer: '))
        if check_answer(question, answer, user_answer):
            correct += 1
    final_score = calculate_score(correct, total_problems)
    print('Your final score is', final_score)


operations = ['+', '-', '*', '/', '**']
math_test(2, operations, 10, 5)
