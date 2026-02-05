# Phishing Email Detection System

## Project Description
This project is developed as part of my Cybersecurity Internship (Minor Project–2).
The objective of this project is to detect phishing emails by analyzing email content for common phishing indicators such as suspicious keywords, malicious links, and abnormal patterns.

Phishing is a common social engineering attack where attackers trick users into revealing sensitive information like passwords or banking details. This project demonstrates a basic rule-based phishing detection approach using Python.

## Tools Used
- Python
- Regular Expressions (Regex)
- Git & GitHub
- VS Code
- Windows Operating System

## Work Done(Setup & Basic Phishing Detection)
- Installed and verified Python environment
- Created a GitHub repository named `hh8-minor-project-2`
- Created project folder and opened it in VS Code
- Initialized Git repository using: `git init`
- Linked local project to GitHub repository
- Implemented a basic phishing detection script using suspicious keywords
- Tested the script with sample phishing and legitimate emails
- Pushed initial code and commits to GitHub

## Work Done(URL & Regex-Based Detection)
- Studied common phishing URL patterns
- Implemented URL detection using regular expressions(Regex)
- Extracted URLs from email content
- Identified suspicious words within URLs such as login, verify and secure
- Classified emails based on the presence of malicious URLs
- Tested the program using sample email inputs
- Uploaded updated code and screenshots to GitHub

## Work Done(Final Phishing Detection Logic)
- Combined keyword-based and URL-based detection techniques
- Implemented a scoring mechanism to reduce false positives
- Classified emails as phishing or legitimate based on total score
- Created the final phishing detection script
- Verified outputs using multiple test cases
- Captured screenshots of final results and pushed to GitHub

## How the System Works
- User enters email content as input
- Program checks for suspicious phishing-related keywords
- URLs are extracted using regex and analyzed
- A phishing score is calculated based on detected patterns
- Email is classified as: Phishing and Legitimate

## How to Run the Project
1. Install Python
2. Navigate to the project folder
3. Run basic phishing detection: `python phishing_basic.py`
4. Run URL-based detection: `python phishing_links.py`
5. Run final phishing detection system: `python phishing_final.py`

## What I Learned
- Understanding phishing and social engineering attacks
- Identifying phishing indicators in emails
- Using regex for URL extraction and analysis
- Implementing rule-based detection logic
- Reducing false positives using combined analysis
- Writing security-focused Python programs
- Using Git and GitHub for version control and progress tracking

## Ethical Note
This project was developed strictly for educational purposes as part of a cybersecurity internship.
All testing was performed using sample or self-created email content, and no real user data was accessed or misused.

## Output Screenshots
Screenshots of: Program execution, Phishing and legitimate email detection results are included in the output folder.

## Conclusion
This project helped me understand how real-world email security systems use rule-based logic as a first layer of phishing detection.