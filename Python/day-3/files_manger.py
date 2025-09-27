# 5) OS File Manager
#    - Ask user for a directory path.
#    - Automatically:
#         - Create a folder "backup" inside it if not exists.
#         - Copy all .txt files into "backup".
#         - Print summary: how many files copied.
#    - If directory invalid, retry until correct.

import os
from time_decorator import log_time
import shutil

@log_time
def file_manager():
    while True:
        path = input("Enter directory path: ").strip()
        if os.path.isdir(path):
            break
        else:
            print("Invalid directory. Try again.")

    backup_path = os.path.join(path, "backup")
    os.makedirs(backup_path, exist_ok=True)

    count = 0
    for file in os.listdir(path):
        if file.endswith(".txt"):
            shutil.copy(os.path.join(path, file), backup_path)
            count += 1

    print(f"{count} .txt files copied to backup/")

if __name__ == "__main__":
    file_manager()
