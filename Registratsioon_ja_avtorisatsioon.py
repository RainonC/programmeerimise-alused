from MyModule import *


while True:
    choice = input("Выберите опцию: 1. Регистрация, 2. Вход, 3. Выход\n")

    if choice == '1':
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        register(username, password)
    elif choice == '2':
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        if login(username, password):
            break
    elif choice == '3':
        break
    else:
        print("Неправильный выбор.")
