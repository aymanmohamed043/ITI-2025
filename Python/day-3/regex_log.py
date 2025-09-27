# 2) Regex Log Cleaner
#    - Create a file called "access.log" with 10 fake log lines
#      (mix valid emails and invalid strings).
#    - Use regex to extract all valid emails.
#    - Save them into "valid_emails.txt".
#    - Print how many unique emails were found.
import re
import re
from time_decorator import log_time

@log_time
def regex_log_cleaner():

    with open("access.log") as f:
        data = f.read()

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", data)
    unique_emails = set(emails)

    with open("output_files/valid_emails.txt", "w") as f:
        f.write("\n".join(unique_emails))

    print(f"Found {len(unique_emails)} unique emails.")


if __name__ == "__main__":
    regex_log_cleaner()
