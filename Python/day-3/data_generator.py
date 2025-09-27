# 6) Random Data Generator
#    - Ask user how many random numbers to generate.
#    - Save them into "random_numbers.csv" as:
#         index,value
#         1, 42
#         2, 87
#         ...
#    - Print total count and average of the generated numbers.

import csv
import random
from time_decorator import log_time

@log_time
def random_data_generator():
    while True:
        try:
            n = int(input("How many random numbers to generate? "))
            if n > 0:
                break
            else:
                print("Enter a positive number.")
        except ValueError:
            print("Invalid input. Enter an integer.")

    numbers = [random.randint(1, 100) for _ in range(n)]

    with open("output_files/random_numbers.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["index", "value"])
        for i, num in enumerate(numbers, 1):
            writer.writerow([i, num])

    avg = sum(numbers) / len(numbers)
    print(f"Generated {n} numbers. Average = {avg:.2f}")

if __name__ == "__main__":
    random_data_generator()
