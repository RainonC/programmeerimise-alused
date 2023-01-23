import random


def get_level():
    while True:
        try:
            ans = int(input("Выберите уровень (1, 2 или 3): "))
            if 1 <= ans <= 3:
                return ans
            else:
                print("Пожалуйста, выберите уровень между 1 и 3.")
        except ValueError:
            print("Пожалуйста, введите число.")


def get_operation(level):
    operations = ["+", "-", "*", "/", "//", "%", "**"]
    if level < 3:
        return random.choice(operations)
    else:
        return random.choice(operations[:2 * level])
    # if level == 1:
    #     operations = operations[:2]
    # elif level == 2:
    #     operations = ["+", "-", "*", "/"]
    # else:
    #     operations = ["+", "-", "*", "/", "//", "%", "**"]
    #     return random.choice(operations)


def get_range(level):
    return 0 - 250 * level, 0 + 250 * level


def get_question(level):
    range_min, range_max = get_range(level)
    num1 = random.randint(range_min, range_max)
    num2 = random.randint(range_min, range_max)
    operation = get_operation(level)
    question = f"{num1} {operation} {num2}"
    answer = eval(question)
    return question, answer


def math_quiz():
    level = get_level()
    correct_answers = 0
    while True:
        try:
            total_questions = int(input("Введите количество заданий: "))
        except ValueError:
            print("Give me num")
        else:
            break
    for i in range(total_questions):
        question, correct_answer = get_question(level)
        user_answer = input(f'{question} = ')
        try:
            user_answer = float(user_answer)
            if user_answer == correct_answer:
                print("Правильно!")
                correct_answers += 1
            else:
                print(f"Неправильно. Правильный ответ: {correct_answer}")
        except ValueError:
            print("Пожалуйста, введите число.")
    score = (correct_answers / total_questions) * 100
    if score >= 90:
        grade = "5"
    elif 75 <= score < 90:
        grade = "4"
    elif 60 <= score < 75:
        grade = "3"
    else:
        grade = "2"
    print(f"Всего было {total_questions} заданий, правильно отвеченно {correct_answers}, ваша оценка {grade}")


math_quiz()
