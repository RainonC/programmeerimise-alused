import random

# Функция для считывания в список данных из файла
def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

# Считываем списки слов из файлов
rus = loe_failist("rus.txt")
ang = loe_failist("ang.txt")

# Функция для перевода слова с русского на английский
def rus_to_eng(word):
    for i in range(len(rus)):
        if rus[i] == word:
            return ang[i]
    return None

# Функция для перевода слова с английского на русский
def eng_to_rus(word):
    for i in range(len(ang)):
        if ang[i] == word:
            return rus[i]
    return None

# Функция для добавления нового слова в словарь
def add_word(word, translation, language):
    if language == "rus":
        rus.append(word)
        ang.append(translation)
    else:
        ang.append(word)
        rus.append(translation)
    with open("rus.txt", "a", encoding="utf-8-sig") as f1, open("ang.txt", "a", encoding="utf-8-sig") as f2:
        f1.write(word + "\n")
        f2.write(translation + "\n")

# Функция для исправления ошибки в словаре
def fix_word(word, translation, language):
    if language == "rus":
        for i in range(len(rus)):
            if rus[i] == word:
                ang[i] = translation
                break
    else:
        for i in range(len(ang)):
            if ang[i] == word:
                rus[i] = translation
                break
    with open("rus.txt", "w", encoding="utf-8-sig") as f1, open("ang.txt", "w", encoding="utf-8-sig") as f2:
        for i in range(len(rus)):
            f1.write(rus[i] + "\n")
            f2.write(ang[i] + "\n")

# Функция для проверки знания слов из словаря
def test_words():
    n = int(input("Введите количество слов для проверки: "))
    words = random.sample(rus, n)
    print("Переведите на английский:")
    correct = 0
    for i in range(n):
        print(words[i])
        answer = input()
        if answer.lower() == rus_to_eng(words[i]).lower():
            print("Верно!")
            correct += 1
        else:
            print("Неверно!")
    print(f"Результат: {correct / n * 100:.2f}%")




