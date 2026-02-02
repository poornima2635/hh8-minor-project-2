phishing_keywords = [
    "urgent",
    "verify",
    "password",
    "click",
    "login",
    "account suspended",
    "confirm"
]

email = input("Enter email content:\n").lower()

found = False
for word in phishing_keywords:
    if word in email:
        print(f" Suspicious keyword detected: {word}")
        found = True

if found:
    print("\nResult: This email is likely PHISHING")
else:
    print("\nResult: This email looks LEGITIMATE")
