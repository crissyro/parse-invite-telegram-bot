import csv

def save_members_to_csv(members: list):
    with open('members.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['user_id', 'username'])
        writer.writerows(members)

def read_members_from_csv():
    with open('members.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        return [row for row in reader]