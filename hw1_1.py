# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.
name = input('ФИО: ')
age = int(input('Ваш возраст: '))
weight = int(input('Ваш вес: '))

if age <= 30 and weight >= 50 and weight <= 120:
    print(f"Хорошее состояние. Ваш возраст {age} год(а)/лет ваш вес {weight} кг.")
elif age > 30 and age <= 40 and (weight < 50 or weight > 120):
    print(f"Займитесь собой. Ваш возраст {age} год(а)/лет ваш вес {weight} кг.")
elif age > 40 and (weight <= 50 or weight >= 120):
    print(f"Сходите к врачу. Ваш возраст {age} год(а)/лет ваш вес {weight} кг.")
else:
    print(f"Ваш возраст {age} год(а)/лет ваш вес {weight} кг.")
