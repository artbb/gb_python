"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""
from functools import reduce

data = [i for i in range(99, 1001) if i % 2 == 0]

data1 = reduce(lambda x, y: x * y, data)  # список длинный, произведение все чисел списка - огромное число

data2 = [i * j for i, j in zip(data, data[1:])]  # дополнительно вывел список с перемножением двух соседних

print(data)
print(data1)
print(data2)
