#Задание 1
indeks = input("Введите почтовый индекс: ")


if not indeks.isdigit() or len(indeks) != 5:
  print("Неправильный формат индекса. Он должен состоять из 5 цифр.")

else:
 
  indeks_list = list(indeks)
  
  
  if indeks_list[0] == "1":
    print("Уезд: Tallinn")
  elif indeks_list[0] == "2":
    print("Уезд: Narva, Narva-Jõesuu")
  elif indeks_list[0] == "3":
    print("Уезд: Kohtla-Järve")
  elif indeks_list[0] in ["4", "5", "6"]:
    print("Оставайтесь дома!")
  else:
    print("Носите маски!")

#Задание 2
original_list = input("Введите исходный список: ").split()
num_elements = int(input("Введите количество меняемых местами элементов: "))


if len(original_list) < 2:
  print("В исходном списке должно быть минимум 2 элемента.")

else:
 
  for i in range(num_elements):
    original_list[i], original_list[-i-1] = original_list[-i-1], original_list[i]

  # Выводим результат
  print("Измененный список:", original_list)

#Задание 3

def find_useless_number(numbers):
  
  max_number = max(numbers)
  
  useless_number = max_number / len(numbers)
  
  numbers[numbers.index(max_number)] = useless_number
  
  return numbers


print(find_useless_number([1, 2, 3, 4, 5])) # [1, 2, 3, 4, 1]
print(find_useless_number([2, 3, 5, 7, 11]))

#Задание 4


def sort_by_absolute_value(numbers, ascending=True):
  
  sorted_numbers = sorted(numbers, key=abs, reverse=not ascending)
  
  return sorted_numbers


print(sort_by_absolute_value([-5, 3, -2, 7, -4])) # [-5, -4, -2, 3, 7]
print(sort_by_absolute_value([-5, 3, -2, 7, -4], ascending=False)) # [7, 3, -2, -4, -5]

#Задание 5


def pad_strings(strings):
  
  max_length = max(map(len, strings))
  
  padded_strings = [string.rjust(max_length, '_') for string in strings]
 
  return padded_strings


print(pad_strings(['крот', 'белка', 'выхухоль'])) # ['крот____', 'белка___', 'выхухоль']
print(pad_strings(['a', 'aa', 'aaa', 'aaaa', 'aaaaa'])) # ['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa']
print(pad_strings(['qweasdqweas', 'q', 'rteww', 'ewqqqqq'])) # ['qweasdqweas', 'q__________', 'rteww______', 'ewqqqqq____']

#Задание 6

name = input("Пожалуйста, введите имя: ")


if name.isalpha():
  
  print(f"Привет, {name.capitalize()}!")

  
  num_letters = len(name)
  print(f"Количество букв в имени: {num_letters}")

  
  num_vowels = 0
  num_consonants = 0
  for letter in name:
    if letter.lower() in "aeiouy":
      num_vowels += 1
    else:
      num_consonants += 1
  print(f"Количество гласных букв: {num_vowels}")
  print(f"Количество согласных букв: {num_consonants}")

  