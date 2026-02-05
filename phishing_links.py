import re

# Regex pattern to find URLs
url_pattern = r"http[s]?://\S+"

# Suspicious words often found in phishing URLs
suspicious_words = [
    "login",
    "verify",
    "secure",
    "account",
    "update",
    "bank",
    "password"
]

email = input("Enter email content:\n").lower()

# Find URLs in the email
urls = re.findall(url_pattern, email)

if not urls:
    print("\nNo URLs found in the email.")
    print("Result: This email looks LEGITIMATE")
else:
    print("\nURLs found in the email:")
    for url in urls:
        print(url)

    phishing_detected = False

    for url in urls:
        for word in suspicious_words:
            if word in url:
                phishing_detected = True
                print(f"\n⚠️ Suspicious word '{word}' found in URL")

    if phishing_detected:
        print("\nResult: This email is likely PHISHING")
    else:
        print("\nResult: This email looks LEGITIMATE")
