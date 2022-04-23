# ---------------- 1 ----------------

my_list = ['hello', 'world', 100, True, None, ['hi', 'there'], (1, 2), {1, 2, 3, 4, 5},
           {'one': 1, 'two': 2}, range(10), frozenset(range(10)), TypeError,
           zip([(1, 2), ('a', 'b')]), b'string', bytearray(b'string')]

for ind, el in enumerate(my_list, start=1):
    print(f'{ind:02}: {el} has type {type(el)}')
    print('-' * 10)

# ---------------- 2 ----------------
numbers = input('введите числа через запятую без пробелов')
my_list = numbers.split(',')

for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(my_list)

# ---------------- 3 ----------------
month_number = int(input('Enter month number'))

seasons_dict = {
    1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer',
    7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}

if month_number in seasons_dict:
    print('it is in', seasons_dict[month_number])
else:
    print('enter a valid month number')

# ---------------- 3 ----------------
month_number = int(input('Enter month number'))

months = [
    ('January', 'Winter'),
    ('February', 'Winter'),
    ('March', 'Spring'),
    ('April', 'Spring'),
    ('May', 'Spring'),
    ('June', 'Summer'),
    ('July', 'Summer'),
    ('August', 'Summer'),
    ('September', 'Autumn'),
    ('October', 'Autumn'),
    ('November', 'Autumn'),
    ('December', 'Winter'),
]

if 0 < month_number <= len(months):
    print('it is in', months[month_number - 1][1])
else:
    print('enter a valid month number')

# ---------------- 4 ----------------
words = input('Enter some words').split()

for ind, word in enumerate(words):
    print(f'{ind:02}: {word:.10}')

# ---------------- 5 ----------------
my_list = [7, 5, 3, 3, 2]

number = int(input('Enter a number'))
if number in my_list:
    index = my_list.index(number)
    my_list.insert(index + 1, number)
else:
    for num in my_list:
        if number > num:
            idx = my_list.index(num)
            my_list.insert(idx, number)
            break

    if number not in my_list:
        my_list.append(number)

print(my_list)

# ---------------- 6 ----------------
warehouse = []
analytics = {
    'name': [],
    'unit': [],
    'quantity': [],
    'price': [],
}

while True:
    name = input('Название товара')
    unit = input('Единицы измерения')
    quantity = input('Количество')
    price = input('Цена')

    product = {
        'name': name,
        'unit': unit,
        'quantity': quantity,
        'price': price,
    }

    warehouse.append((len(warehouse) + 1, product))

    if input('Добавить ещё? (введите да, если хотите продолжить)') != 'да':
        break


for item in warehouse:
    product = item[1]

    for key in analytics:
        if product[key] not in analytics[key]:
            analytics[key].append(product[key])

print(analytics)



