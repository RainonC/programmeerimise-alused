from mymodule import *

while True:

    print("Выберите действие: ")
    print("1. Добавить слово в словарь")
    print("2. Исправить слово в словаре")
    print("3. Проверить знание слов")
    print("4. Выйти из программы")
    choice = input()

    if choice == "1":
        language = input("Выберите язык (rus/eng): ")
        if language == "rus":
            word = input("Введите слово на русском: ")
            translation = input("Введите перевод на английский: ")
        else:
            word = input("Введите слово на английском: ")
            translation = input("Введите перевод на русский: ")
        add_word(word, translation, language)
        print("Слово добавлено в словарь!")

    elif choice == "2":
        language = input("Выберите язык (rus/eng): ")
        if language == "rus":
            word = input("Введите слово на русском: ")
            translation = input("Введите исправленный перевод на английский: ")
        else:
            word = input("Введите слово на английском: ")
            translation = input("Введите исправленный перевод на русский: ")
        fix_word(word, translation, language)
        print("Слово исправлено в словаре!")

    elif choice == "3":
        test_words()

    elif choice == "4":
        print("До свидания!")
        break

    else:
        print("Неверный выбор. Попробуйте еще раз.")


