import re
import random
import string

def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    print("\nSecurity Score:", score, "/6")

    if score <= 1:
        print("Very Weak Password 🔴")
    elif score <= 3:
        print("Weak Password 🟠")
    elif score <= 4:
        print("Medium Password 🟡")
    elif score <= 5:
        print("Strong Password 🟢")
    else:
        print("Very Strong Password 🟢🟢")

    if suggestions:
        print("\nSecurity Recommendations:")
        for item in suggestions:
            print("-", item)

def generate_password(length=12):
    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*()"
    )

    password = "".join(
        random.choice(characters)
        for _ in range(length)
    )

    return password

while True:
    print("\n===== Password Strength Checker =====")
    print("1. Check Password")
    print("2. Generate Secure Password")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        password = input("Enter password: ")
        check_password(password)

    elif choice == "2":
        print("\nSuggested Secure Password:")
        print(generate_password())

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
