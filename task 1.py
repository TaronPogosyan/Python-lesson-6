# 1. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
#   [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def summ(list):
    s = 0
    for i in range(len(list)):
        if i % 2 != 0:
            s += list[i]
    print(f"Ответ: {s}")

list = list(map(int, input("Введите числа через пробел: ").split()))
summ(list)