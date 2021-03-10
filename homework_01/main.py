"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    return [i**2 for i in args]
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(in_list,num_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    if num_type == 'even':
        return [item for item in in_list if (item % 2) == 0 and type(item)==int]
    elif num_type == 'odd':
        return [item for item in in_list if item % 2 != 0 and type(item)==int]
    elif num_type == 'prime':
        list_prime = []
        for num in in_list:
            if  num > 1 and type(num)==int: #check whether it greater than 1 
                for i in range(2,num+1,1):
                    if num % i == 0: 
                        if i != num: # if it is not number itself then break
                            break
                        else:
                            list_prime.append(num)
                            continue
            else:
                continue
        return list_prime
    else:
        raise ValueError("only 'even','odd','prime' number types are availiable")