from random import random, randint, sample
"""
Функція генерує вказану кількість унікальних чисел (quantity) у заданому діапазоні (min - max).
Функція повертає список випадково вибраних, відсортованих чисел. 
Числа в наборі не повинні повторюватися. 
Якщо параметри не відповідають заданим обмеженням, 
функція повертає пустий список
"""
def get_numbers_ticket(min, max, quantity) -> list :
    arr = []
    if (min < 1 or max > 1000) or (min > max) or (quantity > (max-min)):
        return arr
    else:
        while len(arr) != quantity:
            arr.append(randint(min, max))
        return sorted(sample(range(min, max), quantity))

lottery_numbers = get_numbers_ticket(10, 13, 5)
print("Ваші лотерейні числа:", lottery_numbers)
