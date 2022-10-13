# 3 Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

def check(a: int, b: int) -> bool:
    if a > b:
        a, b = b, a
    return a ** 2 == b


def f_sum(a: int, b: int) -> int:
    return a + b
    

if __name__ == "__main__":
    result = check(int(input('Введите первое число: ')),
                   int(input('Введите второе число: ')))
    print(f'Одно число является квадратом другого? {"да" if result else "нет"}')