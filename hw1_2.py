# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.
#time_sec = int(input('Введите время в секундах: '))
#minute = time_sec / 60
#hour = minute / 60
#sec = int((minute - int(minute)) * 60)
#print(f"{time_sec} секунд равно {int(hour)} чч : {int(minute)} мм : {sec} сс")
time_sec = int(input('Введите время в секундах: '))
hour = time_sec // 3600
minute = (time_sec // 60) - hour * 60
sec = time_sec % 60
print(f"{time_sec} секунд равно {hour:02} чч : {minute:02} мм : {sec:02} сс")