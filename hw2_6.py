#6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество,
# единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные
# у пользователя.
#Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.
c_name = []
c_price = []
c_amount = []
c_measure = []
while True:
    c_ask = input('Ввести новый товар?(да/нет): ')
    if c_ask != 'да':
        break
    else:
        c_name.append(input('Введите название товара: '))
        c_price.append(float(input('Введите цену товара, руб.: ')))
        c_amount.append(float(input('Введите количество товара, ед.: ')))
        c_measure.append(input('Введите единицу измерения: '))

product = {
        'название': c_name,
        'цена': c_price,
        'количество': c_amount,
        'eд': c_measure,
    }
p_name = product['название']
p_price = product['цена']
p_amount = product['количество']
p_measure = product['eд']
p_keys = list(product)

print('\n', 'База данных', '\n')

i = 0
for p in p_name:
    i += 1
    c_tuple = (i, {p_keys[0]: p_name[i - 1], p_keys[1]: p_price[i - 1], p_keys[2]: p_amount[i - 1], p_keys[3]: p_measure[i - 1]})
    print(c_tuple)

print('\n', 'Аналитика', '\n')
for key, value in product.items():
    print(key, value)
