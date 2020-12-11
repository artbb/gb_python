# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
number = int(input('Введите любое целое положительное число: '))
number_nn = int((f"{number}{number}"))
number_nnn = int((f"{number}{number}{number}"))

print(f"{number} + {number_nn} + {number_nnn} равно")
print(number + number_nn + number_nnn)
