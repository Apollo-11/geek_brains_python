

#--------------------- 2 ---------------------

seconds = int(input('Enter time in seconds'))

minutes = seconds // 60
hours = minutes // 60

seconds_reminded = seconds % 60
minutes_reminded = minutes % 60

print(f'{hours:02}:{minutes_reminded:02}:{seconds_reminded:02}')


#--------------------- 3 ---------------------
n = input('Enter a number')

print(f'{n} + {n * 2} + {n * 3} = {int(n) + int(n * 2) + int(n * 3)}')


#--------------------- 4 ---------------------

n = int(input('Enter a number'))

while n <= 0:
    print('The number must be greater than 0')
    n = input('Enter a number greater than 0')

if n < 10:
    print(f'Biggest number is {n}')

biggest_num = n % 10

reminder = n // 10

while reminder > 0:
    num = reminder % 10
    if num > biggest_num:
        biggest_num = num

    if biggest_num == 9:
        break

    reminder = reminder // 10

print(f'the biggest number is {biggest_num}')


#--------------------- 5 ---------------------

earnings = int(input('Выручка'))
expenses = int(input('Издержки'))

profit = earnings - expenses

if profit > 0:
    company_size = int(input('Численность сотрудников'))
    profit_per_employee = profit / company_size
    print(f'Фирма заработала {profit}')
    print(f'{profit_per_employee:.2f} на сотрудника')
    print(f'Рентабельность {profit/earnings:.2f}')
elif profit == 0:
    print('Ничего не заработали, но и убытков нет')
else:
    print('Убыткииии ', profit)


#--------------------- 6 ---------------------
initial_result_km = int(input('Сколько километров спортсмен пробежал в первый день'))
goal_km = int(input('Цель в километрах'))

while goal_km <= initial_result_km:
    print('Цель должна быть больше количества километров в первый день')
    initial_result_km = int(input('Сколько километров спортсмен пробежал в первый день'))
    goal_km = int(input('Цель в километрах'))

next_day_result = initial_result_km
days_counter = 1
while goal_km > next_day_result:
    next_day_result = next_day_result * 1.1
    days_counter += 1
    print(days_counter, next_day_result)

print(f'Результат будет достигнут на {days_counter}-й день')




