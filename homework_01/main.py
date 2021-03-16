"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    return [i**2 for i in args]
    


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def prime_process():
    list_prime = []
    for num in in_list:
        if  num > 1 and isinstance(num, int): #check whether it greater than 1 
            for i in range(2,num+1,1):
                if num % i == 0: 
                    if i != num: # if it is not the number itself then break
                        break
                    else: # if it is, then it is our prime number
                        list_prime.append(num)
                        continue
        else:
            continue # in case the number is 1 or not a number
    return list_prime

def filter_numbers(in_list,num_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    if num_type == EVEN:
        return [item for item in in_list if (item % 2) == 0 and isinstance(item, int)]
    elif num_type == ODD:
        return [item for item in in_list if item % 2 != 0 and isinstance(item, int)]
    elif num_type == PRIME:
        return prime_process()
    else:
        raise ValueError("only 'even','odd','prime' number types are available")