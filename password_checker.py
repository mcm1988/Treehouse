import sys
# this is a while loop lesson. do not use this in the real world where passwords or sensitive data is involved

MASTER_PASSWORD = 'opensesame'
password = input("Please enter the super secret password:  ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password, try again:  ")
    attempt_count += 1
print("Welcome to secret town")
