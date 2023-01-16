logins = []
passwords = []

def register(username, password=None):
    """
    Регистрация нового пользователя.Если не вводит пароль-то программа сделает за него свой.
    """
    if password is None:       
        str0 = ".,:;!_*-+()/#¤%&"
        str1 = "0123456789"
        str2 = "abcdefghijklmnopqrstuvwxyz"
        str3 = str2.upper()
        passwd = "".join(random.sample(str0+str1+str2+str3, 8))
    else:
        passwd = password
        
    logins.append(username)
    passwords.append(passwd)
    print(f"Регистрация прошла успешно. Ваш пароль {passwd}")

def login(username, password):
    """
    Проверяет, соответствует ли пароль к пользователю.
    """
    if username in logins:
        index = logins.index(username)
        if passwords[index] == password:
            print("Вход успешен.")
            return True
    print("Неправильный пароль или имя пользователя.")
    return False
