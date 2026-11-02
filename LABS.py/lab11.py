
username = input("Enter your username: ")
password = input("Enter your password: ")

print(" PASSWORD VALIDATION REPORT")

print("Username:", username)
print("Password:", "*" * len(password))

if len(password) >= 8:
    print("[PASS] Minimum 8 characters")
else:
    print("[FAIL] Minimum 8 characters")


if any(char.isdigit() for char in password):
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if any(char.isupper() for char in password):
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

if (len(password) >= 8
    and any(char.isdigit() for char in password)
    and any(char.isupper() for char in password)):

    print("\nPassword is VALID!")
    print("Account created successfully for", username + "!")
else:
    print("\nPassword is INVALID.")

