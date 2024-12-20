import csv

def read_from_csv(csv_path):
    data = []
    with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    print(data)

read_from_csv('cafe-data.csv')
