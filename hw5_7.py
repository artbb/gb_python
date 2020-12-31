"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
"""
import json
with open('hw5_7.file', 'r', encoding='utf-8') as file5_7:
    spisok = []
    dict_f = {}
    dict_a = {}
    summ_pr = []
    for line in file5_7:
        name = line.split()[0]
        pr = int(line.split()[2]) - int(line.split()[3])
        dict_f.update({name: pr})
        if pr > 0:
            summ_pr.append(pr)
    pr_avg = round(sum(summ_pr) / len(summ_pr), 2)
    dict_a.update({'Средняя прибыль: ': pr_avg})
    spisok.append(dict_f)
    spisok.append(dict_a)
    print(spisok)
    json_spisok = open("hw5_7.json", 'w', encoding='utf-8')
    json.dump(spisok, json_spisok, indent=3, ensure_ascii=False)
    json_spisok.close()
