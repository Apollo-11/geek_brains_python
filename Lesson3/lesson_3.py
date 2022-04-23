# ----------- 1 -----------
def divide_by(dividend, divisor):
    try:
        result = int(dividend) / int(divisor)
        return f'{result:.2f}'
    except ZeroDivisionError:
        return 'Dividing by zero is not allowed'
    except TypeError:
        return 'Enter numbers only'


print(divide_by(input('Enter a number'), input('Enter divisor number')))


# ----------- 2 -----------
def user(name, surname, birth_year, city, email, phone):
    return f'{name}, {surname}, {birth_year}, {city}, {email}, {phone}'


print(user(name='Nina', surname='Kraviz', birth_year=1987, city='Moscow', email='nina@mail.ru', phone='89996667788'))


# ----------- 3 -----------
def sum_two_biggest(num_1, num_2, num_3):
    sorted_nums = sorted([int(num_1), int(num_2), int(num_3)])
    return sum(sorted_nums[1:])


print(sum_two_biggest(input(), input(), input()))


# ----------- 4 -----------
def num_to_power_1(num, power):
    try:
        return int(num) ** int(power)
    except TypeError:
        return 'Only numbers allowed!!!'


print(num_to_power_1(input('Enter a number'), input('Power')))


# ----------- 4.2 -----------

def num_to_power_2(num, power):
    try:
        result = 1
        for _ in range(abs(int(power))):
            if int(power) >= 0:
                result *= int(num)
            else:
                result /= int(num)
            print('result', result)
        return result
    except TypeError:
        return 'Only numbers allowed!!!'


print(num_to_power_2(input('Enter a number'), input('Power')))


# ----------- 5 -----------

def get_sum():
    accumulator = 0
    while True:
        string = input('Enter numbers or q to exit')
        for i in string.split():
            if i.lower() == 'q':
                return accumulator
            if i.isdigit():
                accumulator += int(i)

    return accumulator


print(get_sum())


# ----------- 6 - 7 -----------

def int_func(word: str):
    return word.title()


while True:
    word = input('enter a word or q to exit')
    if word.lower() == 'q':
        break

    print(int_func(word))
