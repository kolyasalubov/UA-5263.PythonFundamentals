import tkinter as tk
from random import randint

secret, tries = 0, 10

def reset():
    global secret, tries
    secret, tries = randint(1, 100), 10
    lbl.config(text="Вгадай число від 1 до 100 (10 спроб)", fg="black")
    btn.config(state="normal")
    entry.delete(0, tk.END)

def check(event=None):
    global tries
    if not entry.get().isdigit():
        return lbl.config(text="Введи ціле число!", fg="orange")
    
    guess = int(entry.get())
    entry.delete(0, tk.END)
    tries -= 1

    if guess == secret:
        lbl.config(text=f"Вітаю! Ти вгадав число {secret}!", fg="green")
        btn.config(state="disabled")
    elif tries == 0:
        lbl.config(text=f"Спроби вичерпано! Було загадано {secret}.", fg="red")
        btn.config(state="disabled")
    else:
        hint = "більше" if secret > guess else "менше"
        lbl.config(text=f"Загадане число {hint} за {guess}. Залишилось спроб: {tries}", fg="blue")

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