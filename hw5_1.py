"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка."""

def w_wile(content):
    file1 = open("hw5_1.file", 'a', encoding='utf-8')
    file1.write(f'{content}\n')
    file1.close()
while True:
    content = input('Введите информацию в файл hw5_1.file (для выхода введите q): ')
    if content == 'q':
        break
    w_wile(content)
