"""
4. Создать (не программно) текстовый файл со следующим содержимым:
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл.
"""
with open('hw5_4.file', 'r', encoding='utf-8') as file5_4:
    dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for line in file5_4:
        new_k = [v for k, v in dict.items() if k in line.split()[0]]
        rus = f'{new_k[0]} - {line.split()[2]} \n'
        f_rus = open("hw5_4_rus.file", 'a', encoding='utf-8')
        f_rus.write(rus)
        f_rus.close()
        print(rus)

