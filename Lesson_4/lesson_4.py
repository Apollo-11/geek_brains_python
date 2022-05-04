# ------------ test ------------

from module_1 import sum_integers
from sys import argv

script_name, first_param, second_param, third_param = argv

print(script_name)
print(sum_integers(first_param, second_param, third_param))

lines = [line.strip() for line in open('text.txt')]
print(lines)

my_list = [10, 25, 30, 45, 50]
even_numbers = [num for num in my_list if num % 2 == 0]
print(even_numbers)


# ------------ 1 ------------
from sys import argv

script_name, hours, per_hour, bonus = argv

print(f'The total payment is {(int(hours) * int(per_hour) + int(bonus))}')

# ------------ 2 ------------
numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [number for idx, number in enumerate(numbers) if idx > 0 and numbers[idx] > numbers[idx-1]]
print(result)


# ------------ 3 ------------
print([num for num in range(20, 241) if num % 20 == 0 or num % 21 == 0])


# ------------ 4 ------------
numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [num for num in numbers if numbers.count(num) == 1]

print(result)


# ------------ 5 ------------
from functools import reduce

result = reduce(lambda a, b: a * b, [num for num in range(100, 1001, 2)])

print(result)


# ------------ 6 ------------
from itertools import cycle, count


# 6.1
def print_numbers_from_to(start, stop):
    for i in count(start):
        print(i)
        if i >= stop:
            break


print_numbers_from_to(5, 15)


# 6.2
def print_abc_many_times(symbols_count=10):
    for idx, letter in enumerate(cycle(['a', 'b', 'c'])):
        if idx >= symbols_count:
            break

        print(letter)


print_abc_many_times(symbols_count=10)

# ------------ 7 ------------
from functools import reduce


def fact(number):
    for i in range(1, number + 1):
        yield reduce(lambda a, b: a * b, [num for num in range(1, i + 1)])


for i in fact(10):
    print(i)

