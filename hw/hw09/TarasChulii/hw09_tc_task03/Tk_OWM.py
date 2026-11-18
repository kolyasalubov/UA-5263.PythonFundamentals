import tkinter as tk
from tkinter import font
import OWM
import textwrap

HEIGHT = 350
WIDTH = 450


def show_weather():

    location = entry_field.get().strip()

    if not location:
        label.config(text="Please enter city name")
        return

    try:
        weather = OWM.get_weather(location)
        result = OWM.format_weather(weather)
        label.config(text=result)

    except Exception as e:
        error_test = textwrap.fill(str(e), width=20)
        label.config(text=f"Error: {error_test}")


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application - HW09 - Task03 - UA-5263 - TC")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: show_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
