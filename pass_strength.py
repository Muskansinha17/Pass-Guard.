import string

def evaluate_password_strength(password):
    length_criteria = len(password) >= 8
    lower_criteria = any(c.islower() for c in password)
    upper_criteria = any(c.isupper() for c in password)
    digit_criteria = any(c.isdigit() for c in password)
    special_criteria = any(c in string.punctuation for c in password)

    score = sum([length_criteria, lower_criteria, upper_criteria, digit_criteria, special_criteria])

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    tips = []
    if not length_criteria:
        tips.append("Make it at least 8 characters.")
    if not lower_criteria:
        tips.append("Add lowercase letters.")
    if not upper_criteria:
        tips.append("Add uppercase letters.")
    if not digit_criteria:
        tips.append("Include numbers.")
    if not special_criteria:
        tips.append("Add special characters (e.g., @, #, !).")

    return strength, tips

if __name__ == "__main__":
    print("🔐 Welcome to the Password Strength Evaluator")
    password = input("Enter your password: ")

    strength, suggestions = evaluate_password_strength(password)
    print("\n📝 Evaluation Result:")
    print("Password Strength:", strength)

    if suggestions:
        print("\n💡 Suggestions to improve your password:")
        for tip in suggestions:
            print("-", tip)
    else:
        print("✅ Your password is strong. Good job!")
