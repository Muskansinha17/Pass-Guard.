import tkinter as tk
from tkinter import messagebox
import string

def evaluate_password_strength(password):
    length_criteria = len(password) >= 8
    lower_criteria = any(c.islower() for c in password)
    upper_criteria = any(c.isupper() for c in password)
    digit_criteria = any(c.isdigit() for c in password)
    special_criteria = any(c in string.punctuation for c in password)

    score = sum([length_criteria, lower_criteria, upper_criteria, digit_criteria, special_criteria])

    if score == 5:
        strength = "Strong 💪"
    elif score >= 3:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"

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

# ---------- GUI Setup ----------
def check_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Warning", "Please enter a password.")
        return

    strength, tips = evaluate_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}")

    if tips:
        tips_text = "\n".join(f"• {tip}" for tip in tips)
        tips_label.config(text=f"Suggestions:\n{tips_text}")
    else:
        tips_label.config(text="✅ Your password is strong. Good job!")

# Create main window
root = tk.Tk()
root.title("Password Strength Evaluator")
root.geometry("400x300")
root.resizable(False, False)

# GUI elements
tk.Label(root, text="🔐 Enter Your Password:", font=("Helvetica", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", width=30, font=("Helvetica", 12))
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_password, font=("Helvetica", 12), bg="#4CAF50", fg="white")
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)

tips_label = tk.Label(root, text="", font=("Helvetica", 10), justify="left", wraplength=350, fg="red")
tips_label.pack()

root.mainloop()
