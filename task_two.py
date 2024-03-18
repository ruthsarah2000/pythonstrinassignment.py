'''
2. User Input Data Processor
Task 1: Input Length Validator
Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

Task 2: Password Complexity Checker
Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, contain one uppercase letter, 
one lowercase letter, and one number. If the password does not meet these criteria, print a message explaining the complexity requirements.

Task 3: Email Formatter
Implement a script that ensures all user email addresses are in a standard format
'''

# Task 1 #

def check_name_length(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        print("Error: Both first name and last name should be at least 2 characters long.")
    else:
        print("Both first name and last name are valid.")


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

check_name_length(first_name, last_name)

# Task 2 #

def check_password_complexity(password):
    
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return
    
    
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return
    
    
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        return
    
    
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        return
    
    print("Password complexity requirements met.")
password = input("Enter your password: ")
check_password_complexity(password)

# Task 3 #

import re

def standardize_email_format(emails):
    standardized_emails = []
    
    for email in emails:
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            standardized_emails.append(email.lower())  # Convert to lowercase
        else:
            print(f"Invalid email format: {email}")
    
    return standardized_emails

user_emails = [
    "user@example.com",
    "john.doe@example",
    "jane.doe@example.com",
    "invalid-email"
]

standardized_emails = standardize_email_format(user_emails)
print("Standardized email addresses:")
print(standardized_emails)
