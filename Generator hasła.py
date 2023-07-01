import os
import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(length, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        password_length = int(entry_length.get())

        if password_length < 8 or password_length > 32:
            messagebox.showerror("Error", "Długość hasła powinna wynosić od 8 do 32 znaków.")
            return

        uppercase = check_uppercase.get()
        lowercase = check_lowercase.get()
        digits = check_digits.get()
        special_chars = check_special_chars.get()

        password = generate_password(password_length, uppercase, lowercase, digits, special_chars)

        pyperclip.copy(password)

        label_password.config(text="Wygenerowane hasło: " + password)

    except ValueError:
        messagebox.showerror("Error", "Nieprawidłowa liczba znaków.")

def copy_password():
    password = label_password.cget("text").split(": ")[1]
    pyperclip.copy(password)
    messagebox.showinfo("Sukces", "Hasło zostało skopiowane.")

def save_password():
    password = label_password.cget("text").split(": ")[1]
    try:
        desktop_path = os.path.expanduser("~/Desktop")
        file_path = os.path.join(desktop_path, "haslo.txt")

        with open(file_path, "w") as file:
            file.write(password)

        messagebox.showinfo("Sukces", f"Hasło zostało zapisane do pliku {file_path}.")
    except Exception as e:
        messagebox.showerror("Error", "Wystąpił błąd podczas zapisywania hasła: " + str(e))

def add_copyright_label():
    copyright_text = "© 2023 Szymon Wasik. Wersja 1.0.0"
    copyright_label = tk.Label(root, text=copyright_text, font=("Arial", 10), fg="gray")
    copyright_label.pack(side="bottom", pady=5)

root = tk.Tk()
root.title("Generator hasła")

label_length = tk.Label(root, text="Wprowadź pożądaną długość hasła (od 8 do 32 znaków):")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()

check_uppercase = tk.BooleanVar()
check_uppercase.set(True)
checkbox_uppercase = tk.Checkbutton(root, text="Duże litery", variable=check_uppercase)
checkbox_uppercase.pack()

check_lowercase = tk.BooleanVar()
check_lowercase.set(True)
checkbox_lowercase = tk.Checkbutton(root, text="Małe litery", variable=check_lowercase)
checkbox_lowercase.pack()

check_digits = tk.BooleanVar()
check_digits.set(True)
checkbox_digits = tk.Checkbutton(root, text="Cyfry", variable=check_digits)
checkbox_digits.pack()

check_special_chars = tk.BooleanVar()
check_special_chars.set(True)
checkbox_special_chars = tk.Checkbutton(root, text="Znaki specjalne", variable=check_special_chars)
checkbox_special_chars.pack()

button_generate = tk.Button(root, text="Generuj", command=generate_and_display_password)
button_generate.pack()

label_password = tk.Label(root, text="")
label_password.pack()

button_copy = tk.Button(root, text="Kopiuj", command=copy_password)
button_copy.pack()

button_save = tk.Button(root, text="Zapisz", command=save_password)
button_save.pack()

label_strength = tk.Label(root, text="")
label_strength.pack()

add_copyright_label()
root.mainloop()