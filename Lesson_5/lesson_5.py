# ----------- 1 -----------
file_1 = open('Lesson_5/file_1.txt', 'w')

while True:
    text = input('enter some text')
    if text:
        file_1.write(f'{text}\n')
    else:
        break

file_1.close()


# ----------- 2 -----------
existed_file = open('Lesson_5/ready.txt', 'r')

lines = existed_file.readlines()
lines = list(map(lambda _line: _line.strip(), lines))
print('Lines in the file:', len(lines))
for ind, line in enumerate(lines):
    print(f'words in the line {ind + 1}: {len(line.split())}')

existed_file.close()


# ----------- 3 -----------
with open('Lesson_5/salary.txt', 'r') as salary_data:
    salaries_raw = [tuple(item.strip().split()) for item in salary_data.readlines()]

    salaries = list(map(lambda item: (item[0], float(item[1])), salaries_raw))
    print(salaries)

    low_salaries = []
    total = 0
    for name, salary in salaries:
        if salary < 20000:
            low_salaries.append(name)
        total += salary

    average = total / len(salaries)
    print(f'Average salary is {average:.2f}')
    print('Salaries lower than 20000:')
    for name in low_salaries:
        print(name)


# ----------- 4 -----------
from russian_numerals import prepare

with open('Lesson_5/ready.txt', 'r') as file_1_existed,\
        open('Lesson_5/result.txt', 'w') as result_file:

    lines = [line.strip().split('—') for line in file_1_existed.readlines()]
    lines = list(map(lambda line: (prepare(line[1]), line[1].strip()), lines))

    for word, num in lines:
        result_file.write(f'{word.title()} - {num}\n')


# ----------- 5 -----------
from random import randint
from functools import reduce

numbers = [str(randint(1, 101)) for _ in range(20)]

numbers_file = open('Lesson_5/numbers.txt', 'w+')

numbers_file.write(' '.join(numbers))

numbers_file.seek(0)

numbers_from_file = numbers_file.read().split()

total = reduce(lambda a, b: int(a) + int(b), numbers_from_file, 0)

print(total)


# ----------- 6 -----------
import re
from functools import reduce

with open('Lesson_5/study.txt', 'r') as study_file:
    subjects_of_study = [subject.strip() for subject in study_file.readlines()]

    subjects = {}

    for subject in subjects_of_study:
        name_match = re.search(r'[А-Яа-я\s]+', subject)
        hours_match = re.search(r':\s(.+)', subject)
        if name_match and hours_match:
            hours_line = hours_match[1]
            hours = [int(re.search(r'\d+', time)[0]) for time in hours_line.split() if re.search(r'\d+', time)]
            total_time = reduce(lambda a, b: a + b, hours)

            subjects[name_match[0]] = total_time

    print(subjects)


# ----------- 7 -----------
import json


with open('Lesson_5/firms.txt', 'r') as firms_data, \
        open('Lesson_5/firms.json', 'w') as firms_json:

    firms_list = [firm.strip().split() for firm in firms_data.readlines()]

    firms_dict = {}
    total = 0
    profitable_count = 0

    for firm in firms_list:
        profit = int(firm[2]) - int(firm[3])
        firms_dict[firm[0]] = profit
        if profit > 0:
            total += profit
            profitable_count += 1

    average = total / profitable_count

    firms_dict['average_profit'] = average

    firms_json.write(json.dumps(firms_dict, indent=2))
