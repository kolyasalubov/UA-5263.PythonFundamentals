import tkinter as tk
from random import randint

secret = 0
tries_left = 10


def reset():
    global secret, tries_left
    secret = randint(1, 100)
    tries_left = 10
    lbl.config(text=f"Вгадай число від 1 до 100. Спроб: {tries_left}")
    entry.delete(0, tk.END)
    btn.config(state="normal")


def check(event=None):
    global tries_left

    text = entry.get()
    entry.delete(0, tk.END)

    if not text.isdigit():
        lbl.config(text="Введи число! Спроб: " + str(tries_left))
        return

    guess = int(text)
    tries_left -= 1

    if guess == secret:
        lbl.config(text=f"Вітаю! Вгадав {secret}!")
        btn.config(state="disabled")
    elif tries_left == 0:
        lbl.config(text=f"Програв! Було число {secret}.")
        btn.config(state="disabled")
    elif guess < secret:
        lbl.config(text=f"Загадане число БІЛЬШЕ. Спроб: {tries_left}")
    else:
        lbl.config(text=f"Загадане число МЕНШЕ. Спроб: {tries_left}")


root = tk.Tk()
root.title("Вгадай число")
root.geometry("380x160")

lbl = tk.Label(root, font=("Arial", 11))
lbl.pack(pady=15)

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack()
entry.bind("<Return>", check)

frame = tk.Frame(root)
frame.pack(pady=15)
btn = tk.Button(frame, text="Перевірити", command=check, width=12)
btn.pack(side="left", padx=5)
tk.Button(frame, text="Нова гра", command=reset, width=10).pack(side="left", padx=5)

reset()
root.mainloop()