import csv
import asyncio

async def save_members_to_csv(members: list, filename: str = "members.csv"):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for member in members:
            writer.writerow([member[0], member[1]])

async def read_members_from_csv(filename: str = "members.csv"):
    members = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0].isdigit():
                    members.append((int(row[0]), row[1]))
    except FileNotFoundError:
        pass
    return members