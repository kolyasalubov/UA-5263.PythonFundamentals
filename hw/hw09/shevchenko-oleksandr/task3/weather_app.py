import os
import tkinter as tk
from tkinter import ttk

from pyowm import OWM
from pyowm.commons.exceptions import PyOWMError


class MissingAPIKeyError(Exception):
    pass


def get_weather(city):
    api_key = os.getenv("OWM_API_KEY")
    if not api_key:
        raise MissingAPIKeyError("Set the OWM_API_KEY environment variable first.")

    weather_manager = OWM(api_key).weather_manager()
    weather = weather_manager.weather_at_place(city).weather
    temperature = weather.temperature("celsius")
    wind_speed = weather.wind().get("speed", "unknown")

    return (
        f"City: {city}\n"
        f"Conditions: {weather.detailed_status}\n"
        f"Temperature: {temperature['temp']} °C\n"
        f"Humidity: {weather.humidity}%\n"
        f"Wind: {wind_speed} m/s\n"
        f"Cloudiness: {weather.clouds}%"
    )


def main():
    root = tk.Tk()
    root.title("Weather Application")
    root.geometry("450x350")
    root.minsize(360, 280)

    city_entry = ttk.Entry(root)
    city_entry.insert(0, "London,GB")
    city_entry.pack(fill="x", padx=20, pady=(20, 10))

    result_label = ttk.Label(root, text="Enter a city to get the weather.", anchor="nw")
    result_label.pack(fill="both", expand=True, padx=20, pady=10)

    def show_weather():
        city = city_entry.get().strip()
        if not city:
            result_label.config(text="Enter a city name.")
            return

        try:
            result_label.config(text=get_weather(city))
        except (MissingAPIKeyError, PyOWMError) as error:
            result_label.config(text=f"Unable to get weather: {error}")

    ttk.Button(root, text="Get Weather", command=show_weather).pack(pady=(0, 20))
    root.mainloop()


if __name__ == "__main__":
    main()
