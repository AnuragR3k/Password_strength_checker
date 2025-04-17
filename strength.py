import string

def assess_password_strength(password):
    """
    Assesses the strength of a password based on various criteria.

    Args:
        password (str): The password to assess.

    Returns:
        tuple: A tuple containing the strength level ("Weak", "Moderate", "Strong", "Very Strong")
               and a feedback message with suggestions for improvement if the password is weak.
    """
    score = 0
    feedback = ""

    # Length criteria
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback += "- Increase the length of your password (at least 8 characters).\n"

    # Character type criteria
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if has_uppercase:
        score += 1
    else:
        feedback += "- Include at least one uppercase letter.\n"

    if has_lowercase:
        score += 1
    else:
        feedback += "- Include at least one lowercase letter.\n"

    if has_digit:
        score += 1
    else:
        feedback += "- Include at least one number.\n"

    if has_special:
        score += 1
    else:
        feedback += "- Include at least one special character (e.g., !, @, #, $, %).\n"

    # Overall strength assessment
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    elif score <= 6:
        strength = "Strong"
    else:
        strength = "Very Strong"
        feedback = "Excellent! Your password is very strong."

    if strength != "Very Strong" and not feedback:
        feedback = "Your password meets the basic requirements."

    return strength, feedback

if __name__ == "__main__":
    password = input("Enter the password to assess: ")
    strength, feedback = assess_password_strength(password)
    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Feedback:")
        print(feedback)