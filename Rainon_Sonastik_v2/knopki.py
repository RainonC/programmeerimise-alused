from test1 import *
from mymodule import *
from tkinter import *

# Функция для обработки нажатия на кнопку "Добавить слово"
def add_word_button_pressed():
    language = language_choice.get()
    if language == "rus":
        word = word_entry.get()
        translation = translation_entry.get()
    else:
        word = translation_entry.get()
        translation = word_entry.get()
    add_word(word, translation, language)
    result_label.config(text="Слово добавлено в словарь!", fg="green")

# Функция для обработки нажатия на кнопку "Исправить слово"
def fix_word_button_pressed():
    language = language_choice.get()
    if language == "rus":
        word = word_entry.get()
        translation = translation_entry.get()
    else:
        word = translation_entry.get()
        translation = word_entry.get()
    fix_word(word, translation, language)
    result_label.config(text="Слово исправлено в словаре!", fg="green")

# Функция для обработки нажатия на кнопку "Проверить знание слов"
def test_words_button_pressed():
    test_words()
    result_label.config(text = f"Результат: {correct / n * 100:.2f}%", fg="black")

# Функция для обновления полей ввода при изменении выбранного языка
def language_choice_changed():
    if language_choice.get() == "rus":
        word_label.config(text="Слово на русском:")
        translation_label.config(text="Перевод на английский:")
    else:
        word_label.config(text="Слово на английском:")
        translation_label.config(text="Перевод на русский:")


root = Tk()
root.title("Словарь")


# элементы управления
language_choice = StringVar(value="rus")
language_choice.trace("w", language_choice_changed)
language_rus = Radiobutton(root, text="Русский", variable=language_choice, value="rus")
language_eng = Radiobutton(root, text="Английский", variable=language_choice, value="eng")
word_label = Label(root, text="Слово на русском:")
word_entry = Entry(root)
translation_label = Label(root, text="Перевод на английский:")
translation_entry = Entry(root)
add_word_button = Button(root, text="Добавить слово", command=add_word_button_pressed)
fix_word_button = Button(root, text="Исправить слово", command=fix_word_button_pressed)
test_words_button = Button(root, text="Проверить знание слов", command=test_words_button_pressed)
result_label = Label(root, text="")

#  grid's
language_rus.grid(row=0, column=0, sticky=W)
language_eng.grid(row=0, column=1, sticky=W)
word_label.grid(row=1, column=0, sticky=W)
word_entry.grid(row=1, column=1, sticky=W)
translation_label.grid(row=2, column=0, sticky=W)
translation_entry.grid(row=2, column=1, sticky=W)
add_word_button.grid(row=3, column=0, sticky=W)
fix_word_button.grid(row=3, column=1, sticky=W)
test_words_button.grid(row=4, column=0, sticky=W)
result_label.grid(row=5, column=0, columnspan=2, sticky=W)


root.mainloop()
