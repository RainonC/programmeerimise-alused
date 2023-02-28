import random

#  чтение списка из файлов
def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

# считывание списков из файлов
rus = loe_failist("rus.txt")
ang = loe_failist("ang.txt")

#  перевод слова с русского на английский
def rus_to_eng(word):
    for i in range(len(rus)):
        if rus[i] == word:
            return ang[i]
    return None

#  перевод слова с английского на русский
def eng_to_rus(word):
    for i in range(len(ang)):
        if ang[i] == word:
            return rus[i]
    return None

#  добавление нового слова в словарь
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

#  исправление ошибки в txt файле (словаре)
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
    with open("rus.txt", "w", encoding="utf-8-sig") as rus_file, open("ang.txt", "w", encoding="utf-8-sig") as ang_file:
        for i in range(len(rus)):
            rus_file.write(rus[i] + "\n")
            ang_file.write(ang[i] + "\n")

# тест
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
