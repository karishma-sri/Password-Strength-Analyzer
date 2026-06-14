import tkinter as tk

common_passwords = [
    "password",
    "123456",
    "qwerty",
    "admin",
    "welcome"
]

def check_password():
    password = entry.get()

    suggestions = []
    warnings = []

    if password.lower() in common_passwords:
        warnings.append("Common password detected")

    if len(password) > 0 and len(set(password)) < len(password) / 2:
        warnings.append("Too many repeated characters")

    patterns = ["12345", "qwerty", "abcdef"]

    for p in patterns:
        if p in password.lower():
            warnings.append("Sequential pattern detected")
            break

    score = 0

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase password length (8+ characters)")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if any(not char.isalnum() and not char.isspace() for char in password):
        score += 1
    else:
        suggestions.append("Add special characters")

    
    if score == 5:
        strength = "Highly Strong"
        color = "green"
    elif score == 4:
        strength = "Strong"
        color = "dark green"
    elif score >= 2:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"

    
    result_text = f"Password Score: {score}/5\n"
    result_text += f"Strength: {strength}\n\n"

    if warnings:
        result_text += "Warnings:\n"
        for w in warnings:
            result_text += f"• {w}\n"

    if suggestions:
        result_text += "\nSuggestions:\n"
        for s in suggestions:
            result_text += f"• {s}\n"

    result_label.config(text=result_text, fg=color)



root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x400")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=15)

password_label = tk.Label(root, text="Enter Password:")
password_label.pack()

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=10)


check_button = tk.Button(
    root,
    text="Check Strength",
    command=check_password,
    font=("Arial", 11)
)
check_button.pack(pady=10)


result_label = tk.Label(
    root,
    text="",
    justify="left",
    font=("Arial", 11),
    wraplength=450
)
result_label.pack(pady=20)

root.mainloop()