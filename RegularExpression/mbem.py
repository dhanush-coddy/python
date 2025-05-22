import re

def validate_mobile(number):
    # Validates Indian mobile numbers: 10 digits, starting with 6-9
    pattern = r'^[6-9]\d{9}$'
    return bool(re.fullmatch(pattern, number))

def validate_email(email):
    # Validates standard email format
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return bool(re.fullmatch(pattern, email))

# --- User Input Section ---
mobile_input = input("Enter your mobile number: ")
email_input = input("Enter your email address: ")

print("\n--- Validation Results ---")

if validate_mobile(mobile_input):
    print("Mobile Number is Valid")
else:
    print("Mobile Number is Invalid")

if validate_email(email_input):
    print("Email Address is Valid")
else:
    print("Email Address is Invalid")
