import re
from typing import Tuple

def check_password_strength(password: str) -> Tuple[str, str]:
    score = 0
    feedback = []

    # Length criteria
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase and lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")

    # Numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Final assessment
    if score == 4:
        return "Strong", "Your password is strong."
    elif score == 3:
        return "Moderate", "Your password is moderate. " + " ".join(feedback)
    else:
        return "Weak", 

# Example use case
password = input("Enter a password to test: ")
strength, message = check_password_strength(password)
print(f"Password strength: {strength}")
print(message)