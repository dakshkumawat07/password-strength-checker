

import re

password = input("Enter a password: ")
print(f"Password length: {len(password)}")

score = 0

if len(password) >= 8:
    score += 1

if re.search(r"[A-Z]", password):
    score += 1

if re.search(r"[a-z]", password):
    score += 1

if re.search(r"\d", password):
    score += 1

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

print(f"Security Score: {score}/5")

if score <= 2:
    print("Weak Password 🔴")
elif score <= 4:
    print("Medium Password 🟡")
else:
    print("Strong Password 🟢")

