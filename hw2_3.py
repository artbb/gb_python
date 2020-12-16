#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
try:
    data = int(input('Введите номер месяца (1-12): '))
    month = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
    print('Вариант 1')
    if data == 12 or data == 1 or data == 2:
        print('зима')
    elif data == 3 or data == 4 or data == 5:
        print('весна')
    elif data == 6 or data == 7 or data == 8:
        print('лето')
    elif data == 9 or data == 10 or data == 11:
        print('осень')
    else:
        print('Число должно быть от 1 до 12')

    print('Вариант 2')
    v = list(month.values())
    k = list(month.keys())
    for i in v:
        if data in i:
            v_i = v.index(i)
    print(k[v_i])

except ValueError:
    print('Должно быть число от 1 до 12')
except NameError:
    print('Число должно быть от 1 до 12')
