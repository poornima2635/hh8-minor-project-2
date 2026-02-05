import re

# Phishing-related keywords
phishing_keywords = [
    "urgent",
    "verify",
    "password",
    "click",
    "login",
    "account",
    "confirm",
    "update",
    "suspended"
]

# Suspicious words often found in phishing URLs
suspicious_url_words = [
    "login",
    "verify",
    "secure",
    "account",
    "update",
    "bank",
    "password"
]

# Regex to detect URLs
url_pattern = r"http[s]?://\S+"

email = input("Enter email content:\n").lower()

score = 0

print("\n--- Analysis Started ---")

# Keyword analysis
for word in phishing_keywords:
    if word in email:
        print(f" Suspicious keyword detected: {word}")
        score += 1

# URL analysis
urls = re.findall(url_pattern, email)

if urls:
    print("\nURLs detected in email:")
    for url in urls:
        print(url)
        for suspicious_word in suspicious_url_words:
            if suspicious_word in url:
                print(f"Suspicious word '{suspicious_word}' found in URL")
                score += 1

# Final decision
print("\n--- Analysis Result ---")
print(f"Phishing Score: {score}")

if score >= 2:
    print("Result: This email is likely PHISHING")
else:
    print("Result: This email looks LEGITIMATE")
