"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую
 его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее
функцию int_func()."""
import re


def int_func(text1, text2):
    result_t = text1.capitalize()
    text2 = text2.title().split(' ')
    while '' in text2:
        text2.remove('')
    text_eng = []
    for t in text2:
        if bool(re.search("[А-Яа-я]", t)) is False:
            text_eng.append(t)
    return f'Слово 1 с большой буквы: {result_t}. \nВыборка слов 2 с латинскими буквами: {text_eng}'


print(int_func(text1=input('Введите слово 1 с маленькой буквы: '),
               text2=input('Введите несколько слов 2 через пробел обязательно с латинскими буквами: ')))
