import tkinter as tk
from tkinter import font

from pyowm.commons.exceptions import (
    APIRequestError,
    APIResponseError,
    NotFoundError,
    UnauthorizedError,
)

from OWM import get_weather

HEIGHT = 350
WIDTH = 450


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)



button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: handleSearch())

button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 12), anchor='nw', justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

def handleSearch():
    city = entry_field.get().strip()
    if not city:
        label.config(text="Enter a city name")
        return
    try:
        res = get_weather(city)
    except RuntimeError as e:
        res = str(e)
    except NotFoundError:
        res = f"City not found: {city}"
    except UnauthorizedError:
        res = "Invalid API key"
    except APIRequestError:
        res = "Network error. Check your connection"
    except APIResponseError as e:
        res = f"Weather service error: {e}"
    label.config(text=res)



root.mainloop()

