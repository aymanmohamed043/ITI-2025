# 7) Decorators Task
# - Create a decorator called "log_time" that:
# - Records the execution time of any function.
# - Saves the function name and runtime into "execution_log.txt".
# - Apply this decorator to at least two tasks (e.g., Math Automation & Regex Log Cleaner).
# - Verify that the log file contains entries after running.

import time

def log_time(func):
    """
    Decorator to log execution time of any function.
    Saves function name and runtime into 'execution_log.txt'.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        runtime = end - start

        with open("./output_files/execution_log.txt", "a") as f:
            f.write(f"{func.__name__} executed in {runtime:.4f} ms\n")
        
        return result
    return wrapper
