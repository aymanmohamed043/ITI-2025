from data_generator import random_data_generator
from files_manger import file_manager   
from regex_log import regex_log_cleaner  
from date_reminder import reminder_script
from time_decorator import log_time
from data_transormer import product_transformer
from math_ops import math_operations 

def menu():
    tasks = {
        "1": ("Math Operations", math_operations),
        "2": ("Datetime Reminder Script", reminder_script),
        "3": ("Product Data Transformer", product_transformer),
        "4": ("OS File Manager", file_manager),
        "5": ("Random Data Generator", random_data_generator),
    }

    while True:
        print("\n=== MAIN MENU ===")
        for k, v in tasks.items():
            print(f"{k}. {v[0]}")
        choice = input("Select a task number (or 'q' to quit): ").strip()

        if choice.lower() == "q":
            print("Exiting program.")
            break
        elif choice in tasks:
            tasks[choice][1]()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
