"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""
from termcolor import colored


class NumberError(Exception):
    def __init__(self, number):
        self.number = number


class MainStore():
    def __init__(self):
        self.m_store = {1: 'склад', 2: 'Отдел IT', 3: 'Отдел Финансов', 4: 'Отдел Клиентов'}


class OfficeEq(MainStore):
    def __init__(self):
        super(OfficeEq, self).__init__()
        self.c_type = {1: 'ноутбук', 2: 'МФО', 3: 'Компьютер', 4: 'монитор'}
        self.m_c_1name_amount = []  # ноут_склад
        self.m_c_2name_amount = []  # ноут_IT
        self.m_c_3name_amount = []  # ноут_фин
        self.m_c_4name_amount = []  # ноут_клиент
        self.m_c_5name_amount = []  # мфо_склад
        self.m_c_6name_amount = []  # мфо_IT
        self.m_c_7name_amount = []  # мфо_фин
        self.m_c_8name_amount = []  # мфо_клиент
        self.m_c_9name_amount = []  # комп_склад
        self.m_c_10name_amount = []  # комп_IT
        self.m_c_11name_amount = []  # комп_фин
        self.m_c_12name_amount = []  # комп_клиент
        self.m_c_13name_amount = []  # моник_склад
        self.m_c_14name_amount = []  # моник_IT
        self.m_c_15name_amount = []  # моник_фин
        self.m_c_16name_amount = []  # моник_клиент

    def buy(self):
        c_name = []
        c_price = []
        c_amount = []
        c_measure = []
        c_store = []

        while True:
            c_ask = input('Купить новый товар?(да/нет): ')
            if c_ask != 'да':
                break
            else:
                try:
                    c1 = int(input('Выберите товар (1-ноутбук, 2-МФО, 3-Компьютер, 4-монитор): '))
                    c_name.append(c1)
                except ValueError:
                    print(colored("Ошибка! Введите число", "grey", "on_red"))
                c2 = float(input('Введите цену товара, руб.: '))
                c_price.append(c2)
                c3 = float(input('Введите количество товара, ед.: '))
                c_amount.append(c3)
                c4 = input('Введите описание товара: ')
                c_measure.append(c4)
                c5 = int(input('Выберите подразделение (1-склад, 2-Отдел IT, 3-Отдел Финансов, 4-Отдел Клиентов): '))
                c_store.append(c5)

        product = {
            'тип товара': c_name,
            'цена': c_price,
            'количество': c_amount,
            'описание': c_measure,
            'хранение': c_store
        }
        p_name = product['тип товара']
        p_price = product['цена']
        p_amount = product['количество']
        p_measure = product['описание']
        p_store = product['хранение']
        p_keys = list(product)

        i = 0
        for p in p_name:
            i += 1
            c_tuple = (
                i,
                {p_keys[0]: self.c_type.get(int(p_name[i - 1])), p_keys[1]: p_price[i - 1], p_keys[2]: p_amount[i - 1],
                 p_keys[3]: p_measure[i - 1], p_keys[4]: self.m_store.get(int(p_store[i - 1]))})
            print(c_tuple)
            if p_name[i - 1] == 1 and p_store[i - 1] == 1:
                self.m_c_1name_amount.append(p_amount[i - 1])
            if p_name[i - 1] == 1 and p_store[i - 1] == 2:
                self.m_c_2name_amount.append(p_amount[i - 1])
            if p_name[i - 1] == 1 and p_store[i - 1] == 3:
                self.m_c_3name_amount.append(p_amount[i - 1])
            if p_name[i - 1] == 1 and p_store[i - 1] == 4:
                self.m_c_4name_amount.append(p_amount[i - 1])
            if p_name[i - 1] == 2 and p_store[i - 1] == 1:
                self.m_c_5name_amount.append(p_amount[i - 1])
            if p_name[i - 1] == 2 and p_store[i - 1] == 2:
                self.m_c_6name_amount.append(p_amount[i - 1])
            if p_name[i - 1] == 2 and p_store[i - 1] == 3:
                self.m_c_7name_amount.append(p_amount[i - 1])
            if p_name[i - 1] == 2 and p_store[i - 1] == 4:
                self.m_c_8name_amount.append(p_amount[i - 1])
            if p_name[i - 1] == 3 and p_store[i - 1] == 1:
                self.m_c_9name_amount.append(p_amount[i - 1])
            if p_name[i - 1] == 3 and p_store[i - 1] == 2:
                self.m_c_10name_amount.append(p_amount[i - 1])
            if p_name[i - 1] == 3 and p_store[i - 1] == 3:
                self.m_c_11name_amount.append(p_amount[i - 1])
            if p_name[i - 1] == 3 and p_store[i - 1] == 4:
                self.m_c_12name_amount.append(p_amount[i - 1])
            if p_name[i - 1] == 4 and p_store[i - 1] == 1:
                self.m_c_13name_amount.append(p_amount[i - 1])
            if p_name[i - 1] == 4 and p_store[i - 1] == 2:
                self.m_c_14name_amount.append(p_amount[i - 1])
            if p_name[i - 1] == 4 and p_store[i - 1] == 3:
                self.m_c_15name_amount.append(p_amount[i - 1])
            if p_name[i - 1] == 4 and p_store[i - 1] == 4:
                self.m_c_16name_amount.append(p_amount[i - 1])

        print(f'Остаток ноут склад: {sum(self.m_c_1name_amount)}')
        print(f'Остаток ноут IT: {sum(self.m_c_2name_amount)}')
        print(f'Остаток ноут фин: {sum(self.m_c_3name_amount)}')
        print(f'Остаток ноут клиент: {sum(self.m_c_4name_amount)}')
        print(f'Остаток мфо склад: {sum(self.m_c_5name_amount)}')
        print(f'Остаток мфо it: {sum(self.m_c_6name_amount)}')
        print(f'Остаток мфо фин: {sum(self.m_c_7name_amount)}')
        print(f'Остаток мфо клиент: {sum(self.m_c_8name_amount)}')
        print(f'Остаток комп склад: {sum(self.m_c_9name_amount)}')
        print(f'Остаток комп it: {sum(self.m_c_10name_amount)}')
        print(f'Остаток комп фин: {sum(self.m_c_11name_amount)}')
        print(f'Остаток комп клиент: {sum(self.m_c_12name_amount)}')
        print(f'Остаток моник склад: {sum(self.m_c_13name_amount)}')
        print(f'Остаток моник it: {sum(self.m_c_14name_amount)}')
        print(f'Остаток моник фин: {sum(self.m_c_15name_amount)}')
        print(f'Остаток моник клиент: {sum(self.m_c_16name_amount)}')

    def move(self):
        while True:
            c_ask = input('Переместить товар в отдел?(да/нет): ')
            if c_ask != 'да':
                break
            else:
                m_name = (
                    int(input('Выберите товар, который переместить (1-ноутбук, 2-МФО, 3-Компьютер, 4-монитор): ')))
                m_amount = (int(input('Введите количество: ')))
                m_store1 = (
                    int(input(
                        'Выберите подразделение откуда (1-склад, 2-Отдел IT, 3-Отдел Финансов, 4-Отдел Клиентов): ')))
                m_store2 = (
                    int(input(
                        'Выберите подразделение куда (1-склад, 2-Отдел IT, 3-Отдел Финансов, 4-Отдел Клиентов): ')))
                # ноут из склада по отделам
                if m_store1 == 1 and m_name == 1 and m_store2 == 2:
                    if int(sum(self.m_c_1name_amount)) >= m_amount:
                        self.m_c_1name_amount.append(-m_amount)
                        self.m_c_2name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 1 and m_name == 1 and m_store2 == 3:
                    if int(sum(self.m_c_1name_amount)) >= m_amount:
                        self.m_c_1name_amount.append(-m_amount)
                        self.m_c_3name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 1 and m_name == 1 and m_store2 == 4:
                    if int(sum(self.m_c_1name_amount)) >= m_amount:
                        self.m_c_1name_amount.append(-m_amount)
                        self.m_c_4name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                # ноут из IT по отделам
                if m_store1 == 2 and m_name == 1 and m_store2 == 1:
                    if int(sum(self.m_c_2name_amount)) >= m_amount:
                        self.m_c_2name_amount.append(-m_amount)
                        self.m_c_1name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 2 and m_name == 1 and m_store2 == 3:
                    if int(sum(self.m_c_2name_amount)) >= m_amount:
                        self.m_c_2name_amount.append(-m_amount)
                        self.m_c_3name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 2 and m_name == 1 and m_store2 == 4:
                    if int(sum(self.m_c_2name_amount)) >= m_amount:
                        self.m_c_2name_amount.append(-m_amount)
                        self.m_c_4name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                # ноут из фин по отделам
                if m_store1 == 3 and m_name == 1 and m_store2 == 1:
                    if int(sum(self.m_c_3name_amount)) >= m_amount:
                        self.m_c_3name_amount.append(-m_amount)
                        self.m_c_1name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 3 and m_name == 1 and m_store2 == 2:
                    if int(sum(self.m_c_3name_amount)) >= m_amount:
                        self.m_c_3name_amount.append(-m_amount)
                        self.m_c_2name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 3 and m_name == 1 and m_store2 == 4:
                    if int(sum(self.m_c_3name_amount)) >= m_amount:
                        self.m_c_3name_amount.append(-m_amount)
                        self.m_c_4name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')

                # ноут из клиент по отделам
                if m_store1 == 4 and m_name == 1 and m_store2 == 1:
                    if int(sum(self.m_c_4name_amount)) >= m_amount:
                        self.m_c_4name_amount.append(-m_amount)
                        self.m_c_1name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 4 and m_name == 1 and m_store2 == 2:
                    if int(sum(self.m_c_4name_amount)) >= m_amount:
                        self.m_c_4name_amount.append(-m_amount)
                        self.m_c_2name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 4 and m_name == 1 and m_store2 == 3:
                    if int(sum(self.m_c_4name_amount)) >= m_amount:
                        self.m_c_4name_amount.append(-m_amount)
                        self.m_c_3name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')

                # мфо из склад по отделам
                if m_store1 == 1 and m_name == 2 and m_store2 == 2:
                    if int(sum(self.m_c_5name_amount)) >= m_amount:
                        self.m_c_5name_amount.append(-m_amount)
                        self.m_c_6name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 1 and m_name == 2 and m_store2 == 3:
                    if int(sum(self.m_c_5name_amount)) >= m_amount:
                        self.m_c_5name_amount.append(-m_amount)
                        self.m_c_7name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 1 and m_name == 2 and m_store2 == 4:
                    if int(sum(self.m_c_5name_amount)) >= m_amount:
                        self.m_c_5name_amount.append(-m_amount)
                        self.m_c_8name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')

                # мфо из IT по отделам
                if m_store1 == 2 and m_name == 2 and m_store2 == 1:
                    if int(sum(self.m_c_6name_amount)) >= m_amount:
                        self.m_c_6name_amount.append(-m_amount)
                        self.m_c_5name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 2 and m_name == 2 and m_store2 == 3:
                    if int(sum(self.m_c_6name_amount)) >= m_amount:
                        self.m_c_6name_amount.append(-m_amount)
                        self.m_c_7name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 2 and m_name == 2 and m_store2 == 4:
                    if int(sum(self.m_c_6name_amount)) >= m_amount:
                        self.m_c_6name_amount.append(-m_amount)
                        self.m_c_8name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')

                # мфо из фин по отделам
                if m_store1 == 3 and m_name == 2 and m_store2 == 1:
                    if int(sum(self.m_c_7name_amount)) >= m_amount:
                        self.m_c_7name_amount.append(-m_amount)
                        self.m_c_5name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 3 and m_name == 2 and m_store2 == 2:
                    if int(sum(self.m_c_7name_amount)) >= m_amount:
                        self.m_c_7name_amount.append(-m_amount)
                        self.m_c_6name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 3 and m_name == 2 and m_store2 == 4:
                    if int(sum(self.m_c_7name_amount)) >= m_amount:
                        self.m_c_7name_amount.append(-m_amount)
                        self.m_c_8name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')

                # мфо из клиент по отделам
                if m_store1 == 4 and m_name == 2 and m_store2 == 1:
                    if int(sum(self.m_c_8name_amount)) >= m_amount:
                        self.m_c_8name_amount.append(-m_amount)
                        self.m_c_5name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 4 and m_name == 2 and m_store2 == 2:
                    if int(sum(self.m_c_8name_amount)) >= m_amount:
                        self.m_c_8name_amount.append(-m_amount)
                        self.m_c_6name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 4 and m_name == 2 and m_store2 == 3:
                    if int(sum(self.m_c_8name_amount)) >= m_amount:
                        self.m_c_8name_amount.append(-m_amount)
                        self.m_c_7name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')

                # комп из склад по отделам
                if m_store1 == 1 and m_name == 3 and m_store2 == 2:
                    if int(sum(self.m_c_9name_amount)) >= m_amount:
                        self.m_c_9name_amount.append(-m_amount)
                        self.m_c_10name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 1 and m_name == 3 and m_store2 == 3:
                    if int(sum(self.m_c_9name_amount)) >= m_amount:
                        self.m_c_9name_amount.append(-m_amount)
                        self.m_c_11name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 1 and m_name == 3 and m_store2 == 4:
                    if int(sum(self.m_c_9name_amount)) >= m_amount:
                        self.m_c_9name_amount.append(-m_amount)
                        self.m_c_12name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')

                # комп из it по отделам
                if m_store1 == 2 and m_name == 3 and m_store2 == 1:
                    if int(sum(self.m_c_9name_amount)) >= m_amount:
                        self.m_c_10name_amount.append(-m_amount)
                        self.m_c_9name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 2 and m_name == 3 and m_store2 == 3:
                    if int(sum(self.m_c_9name_amount)) >= m_amount:
                        self.m_c_10name_amount.append(-m_amount)
                        self.m_c_11name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 2 and m_name == 3 and m_store2 == 4:
                    if int(sum(self.m_c_9name_amount)) >= m_amount:
                        self.m_c_10name_amount.append(-m_amount)
                        self.m_c_12name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')

                # комп из фин по отделам
                if m_store1 == 3 and m_name == 3 and m_store2 == 1:
                    if int(sum(self.m_c_11name_amount)) >= m_amount:
                        self.m_c_11name_amount.append(-m_amount)
                        self.m_c_9name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 3 and m_name == 3 and m_store2 == 2:
                    if int(sum(self.m_c_11name_amount)) >= m_amount:
                        self.m_c_11name_amount.append(-m_amount)
                        self.m_c_10name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 3 and m_name == 3 and m_store2 == 4:
                    if int(sum(self.m_c_11name_amount)) >= m_amount:
                        self.m_c_11name_amount.append(-m_amount)
                        self.m_c_12name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')

                # комп из клиент по отделам
                if m_store1 == 4 and m_name == 3 and m_store2 == 1:
                    if int(sum(self.m_c_12name_amount)) >= m_amount:
                        self.m_c_12name_amount.append(-m_amount)
                        self.m_c_9name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 4 and m_name == 3 and m_store2 == 2:
                    if int(sum(self.m_c_12name_amount)) >= m_amount:
                        self.m_c_12name_amount.append(-m_amount)
                        self.m_c_10name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 4 and m_name == 3 and m_store2 == 3:
                    if int(sum(self.m_c_12name_amount)) >= m_amount:
                        self.m_c_12name_amount.append(-m_amount)
                        self.m_c_11name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')

                # мон из склад по отделам
                if m_store1 == 1 and m_name == 4 and m_store2 == 2:
                    if int(sum(self.m_c_13name_amount)) >= m_amount:
                        self.m_c_13name_amount.append(-m_amount)
                        self.m_c_14name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 1 and m_name == 4 and m_store2 == 3:
                    if int(sum(self.m_c_13name_amount)) >= m_amount:
                        self.m_c_13name_amount.append(-m_amount)
                        self.m_c_15name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 1 and m_name == 4 and m_store2 == 4:
                    if int(sum(self.m_c_13name_amount)) >= m_amount:
                        self.m_c_13name_amount.append(-m_amount)
                        self.m_c_16name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')

                # монит из it по отделам
                if m_store1 == 2 and m_name == 4 and m_store2 == 1:
                    if int(sum(self.m_c_14name_amount)) >= m_amount:
                        self.m_c_14name_amount.append(-m_amount)
                        self.m_c_13name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 2 and m_name == 4 and m_store2 == 3:
                    if int(sum(self.m_c_14name_amount)) >= m_amount:
                        self.m_c_14name_amount.append(-m_amount)
                        self.m_c_15name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 2 and m_name == 4 and m_store2 == 4:
                    if int(sum(self.m_c_14name_amount)) >= m_amount:
                        self.m_c_14name_amount.append(-m_amount)
                        self.m_c_16name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')

                # монит из фин по отделам
                if m_store1 == 3 and m_name == 4 and m_store2 == 1:
                    if int(sum(self.m_c_15name_amount)) >= m_amount:
                        self.m_c_15name_amount.append(-m_amount)
                        self.m_c_13name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 3 and m_name == 4 and m_store2 == 2:
                    if int(sum(self.m_c_15name_amount)) >= m_amount:
                        self.m_c_15name_amount.append(-m_amount)
                        self.m_c_14name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 3 and m_name == 4 and m_store2 == 4:
                    if int(sum(self.m_c_15name_amount)) >= m_amount:
                        self.m_c_15name_amount.append(-m_amount)
                        self.m_c_16name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')

                # монит из клиент по отделам
                if m_store1 == 4 and m_name == 4 and m_store2 == 1:
                    if int(sum(self.m_c_16name_amount)) >= m_amount:
                        self.m_c_16name_amount.append(-m_amount)
                        self.m_c_13name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 4 and m_name == 4 and m_store2 == 2:
                    if int(sum(self.m_c_16name_amount)) >= m_amount:
                        self.m_c_16name_amount.append(-m_amount)
                        self.m_c_14name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')
                if m_store1 == 4 and m_name == 4 and m_store2 == 3:
                    if int(sum(self.m_c_16name_amount)) >= m_amount:
                        self.m_c_16name_amount.append(-m_amount)
                        self.m_c_15name_amount.append(m_amount)
                    else:
                        print('Выбранного товара на складе в указанном количестве нет')

        print(f'Остаток ноут склад: {sum(self.m_c_1name_amount)}')
        print(f'Остаток ноут IT: {sum(self.m_c_2name_amount)}')
        print(f'Остаток ноут фин: {sum(self.m_c_3name_amount)}')
        print(f'Остаток ноут клиент: {sum(self.m_c_4name_amount)}')
        print(f'Остаток мфо склад: {sum(self.m_c_5name_amount)}')
        print(f'Остаток мфо it: {sum(self.m_c_6name_amount)}')
        print(f'Остаток мфо фин: {sum(self.m_c_7name_amount)}')
        print(f'Остаток мфо клиент: {sum(self.m_c_8name_amount)}')
        print(f'Остаток комп склад: {sum(self.m_c_9name_amount)}')
        print(f'Остаток комп it: {sum(self.m_c_10name_amount)}')
        print(f'Остаток комп фин: {sum(self.m_c_11name_amount)}')
        print(f'Остаток комп клиент: {sum(self.m_c_12name_amount)}')
        print(f'Остаток моник склад: {sum(self.m_c_13name_amount)}')
        print(f'Остаток моник it: {sum(self.m_c_14name_amount)}')
        print(f'Остаток моник фин: {sum(self.m_c_15name_amount)}')
        print(f'Остаток моник клиент: {sum(self.m_c_16name_amount)}')


start = OfficeEq()
start.buy()
start.move()
