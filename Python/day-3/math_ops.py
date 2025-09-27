# 1) Math Automation
#    - Create a file called "math_report.txt".
#    - Ask the user for multiple numbers (comma-separated).
#    - For each number, calculate:
#         - floor, ceil, square root, area of a circle
#    - Write the results into "math_report.txt".
#    - Confirm file was created and print its content.

import math
from time_decorator import log_time

@log_time
def math_operations():
    while True:
        try:
            # Input inside try so ValueError is caught
            user_input = list(map(float, input("Enter numbers (comma-separated): ").split(",")))

            with open("./output_files/math_report.txt", "w") as file:
                for num in user_input:
                    floor_val = math.floor(num)
                    ceil_val = math.ceil(num)
                    sqrt_val = math.sqrt(num)
                    area_circle = math.pi * (num ** 2)
                    file.write(f"Number: {num}\n")
                    file.write(f"Floor: {floor_val}\n")
                    file.write(f"Ceil: {ceil_val}\n")
                    file.write(f"Square Root: {sqrt_val}\n")
                    file.write(f"Area of Circle: {area_circle}\n\n")
            
            print("math_report.txt created successfully.")
            with open("./output_files/math_report.txt", "r") as file:
                content = file.read()
                print("File Content:")
                print(content)

            break  # exit loop if everything is fine

        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    math_operations()
