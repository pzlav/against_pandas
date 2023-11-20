import csv
import random
from datetime import datetime
from faker import Faker


# Predefined data
fake = Faker()
users = [fake.name() for i in range(100)]     # 100 unique users
objects = [fake.word() for _ in range(1000)]  # 1000 unique object names

# Function to generate a random datetime from 2022
def random_datetime_2022():
    return datetime(2022, random.randint(1, 12), random.randint(1, 28),
                    random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))

# Function to write a batch of rows to the CSV
def write_batch(writer, num_rows):
    for _ in range(num_rows):
        row = [
            random_datetime_2022(),
            random.choice(users),
            random.choice(objects),
            random.uniform(0, 100)
        ]
        writer.writerow(row)


def generate_file(filename, num_rows = 20_000_000, batch_size = 10_000_000):
    # Writing the CSV in batches
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["datetime", "username", "object_name", "value"])  # Header

        for _ in range(num_rows // batch_size):
            write_batch(writer, batch_size)
            print(f"Written batch of {batch_size} rows...")
    print(f"{filename} CSV generation completed.")
    

generate_file('large_dataset', 20_000_000)
generate_file('huge_dataset', 200_000_000)
generate_file('enormous_dataset', 1_000_000_000)
