import tkinter as tk
import tkinter.font as tkfont

from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError, PyOWMError

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

WIDTH = 450
HEIGHT = 380

# Colors
BG = '#1a110c'        # very dark brown window background
CARD = '#2a1c14'      # result card
INPUT = '#3b2a20'     # entry field
ACCENT = '#e8b4a0'    # pink-gold: button / temperature / highlights
ACCENT_HOVER = '#f3cdbf'
TEXT = '#ffffff'      # white text
MUTED = '#d4a897'     # softer pink-gold for secondary text
ERROR = '#ff8a7a'

owm = OWM(API_KEY)
mgr = owm.weather_manager()



def pick_font(*names):
    """Return the first font family installed in the system."""
    installed = set(tkfont.families())
    return next((name for name in names if name in installed), 'TkDefaultFont')


def show_message(text, color=MUTED):
    """Show a single message in the card and clear weather fields."""
    city_label.config(text='')
    temp_label.config(text='')
    status_label.config(text=text, fg=color)
    details_label.config(text='')


def get_weather(event=None):
    """Get current weather for the city from the entry field and show it in the card."""
    city = entry_field.get().strip()
    if not city:
        show_message('Enter a city name')
        return

    try:
        observation = mgr.weather_at_place(city)
    except NotFoundError:
        show_message(f"City '{city}' not found", ERROR)
        return
    except PyOWMError:
        show_message('Could not get weather.\nCheck internet or API key', ERROR)
        return

    w = observation.weather
    city_label.config(text=f'{observation.location.name}, {observation.location.country}')
    temp_label.config(text=f"{round(w.temperature('celsius')['temp'])}°C")
    status_label.config(text=w.detailed_status.capitalize(), fg=MUTED)
    details_label.config(text=f"Humidity {w.humidity}%   ·   "
                              f"Wind {w.wind()['speed']} m/s   ·   "
                              f"Clouds {w.clouds}%")


root = tk.Tk()
root.title('Weather Application')
root.geometry(f'{WIDTH}x{HEIGHT}')
root.resizable(False, False)
root.configure(bg=BG)

FONT = pick_font('Segoe UI', 'Helvetica Neue', 'Helvetica', 'DejaVu Sans')

# Title
tk.Label(root, text='Weather', font=(FONT, 20, 'bold'),
         bg=BG, fg=TEXT).pack(pady=(20, 12))

# Search row
search_frame = tk.Frame(root, bg=BG)
search_frame.pack(padx=30, fill='x')

entry_field = tk.Entry(search_frame, font=(FONT, 12), bg=INPUT, fg=TEXT,
                       insertbackground=TEXT, relief='flat',
                       highlightthickness=2, highlightbackground=INPUT,
                       highlightcolor=ACCENT)
entry_field.pack(side='left', fill='x', expand=True, ipady=6, padx=(0, 10))
entry_field.bind('<Return>', get_weather)
entry_field.focus()

button = tk.Button(search_frame, text='Get Weather', font=(FONT, 10, 'bold'),
                   bg=ACCENT, fg=BG, activebackground=ACCENT_HOVER,
                   activeforeground=BG, relief='flat', bd=0,
                   cursor='hand2', padx=14, pady=6, command=get_weather)
button.pack(side='right')

# Result card
card = tk.Frame(root, bg=CARD)
card.pack(padx=30, pady=20, fill='both', expand=True)

city_label = tk.Label(card, font=(FONT, 16, 'bold'), bg=CARD, fg=TEXT)
city_label.pack(pady=(18, 0))

temp_label = tk.Label(card, font=(FONT, 40, 'bold'), bg=CARD, fg=ACCENT)
temp_label.pack()

status_label = tk.Label(card, font=(FONT, 12), bg=CARD, fg=MUTED)
status_label.pack()

details_label = tk.Label(card, font=(FONT, 10), bg=CARD, fg=TEXT)
details_label.pack(pady=(10, 0))

show_message('Type a city and press Enter')

root.mainloop()