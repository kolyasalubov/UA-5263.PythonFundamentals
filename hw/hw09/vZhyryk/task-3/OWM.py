from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------



# Search for current weather in London (Great Britain) and get details

def get_weather(searchVal: str) -> str:
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(searchVal)
    w = observation.weather
    loc = observation.location
    temp = w.temperature('celsius')
    wind = w.wind()

    return (
        f"{loc.name}, {loc.country}\n"
        f"{w.detailed_status}\n"
        f"Temp: {temp['temp']:.1f}°C (feels {temp['feels_like']:.1f}°C)\n"
        f"Min/Max: {temp['temp_min']:.1f} / {temp['temp_max']:.1f}°C\n"
        f"Wind: {wind['speed']} m/s\n"
        f"Humidity: {w.humidity:.1f}%\n"
        f"Clouds: {w.clouds}%"
    )
