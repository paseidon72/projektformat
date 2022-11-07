import json
import csv


with open('task_1.json') as f:
    output_data = json.load(f)

phone = [
    {
        'phone': (
            {}
        )
    }
]

with open('task_2.csv', 'w', encoding='utf-8') as f:
    file_writer = csv.writer(f)
    for item in (output_data, phone):
        file_writer.writerow(item)

with open('task_2.csv', encoding='utf-8') as f:
    file_reader = csv.reader(f)
    for item in file_reader:
        print(item)


