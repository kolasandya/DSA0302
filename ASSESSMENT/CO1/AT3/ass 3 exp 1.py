import re

# User Input
email = input("Enter Email: ")
password = input("Enter Password: ")
mobile = input("Enter Mobile Number: ")

# Regular Expression Patterns
email_pattern = r'^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.(com|org|edu|net|in)$'

password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!]).{8,}$'

mobile_pattern = r'^[6-9][0-9]{9}$'

# Email Validation
if re.match(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

# Password Validation
if re.match(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password")

# Mobile Validation
if re.match(mobile_pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
