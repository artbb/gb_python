"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже
подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу."""

def my_proga():
    data = []
    while True:
        number = input('Введите строку чисел с пробелами (для выхода наберите q): ')
        number = number.split(' ')
        while '' in number:
            number.remove('')
        summ = 0
        for i in number:
            if i != 'q':
                i = int(i)
                summ += i
            else:
                i == 0
                break
        if 'q' in number:
            print('Введенный массив:', number)
            data.append(summ)
            print('Промежуточный массив из сумм:', data)
            print('Сумма промежуточных массивов:', sum(data))
            print('Вы вышли из программы')
            break
        print('Введенный массив:', number)
        data.append(summ)
        print('Промежуточный массив из сумм:', data)
        print('Сумма промежуточных массивов:', sum(data))


try:
    my_proga()
except ValueError:
    print('Ошибка! Введите числа или q для выхода. Повторить:')
    my_proga()