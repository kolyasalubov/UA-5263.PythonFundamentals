import os

from pyowm import OWM


def get_weather(searchVal: str) -> str:
    api_key = os.environ.get("vZhyryk_OWM_API_KEY")
    if not api_key:
        raise RuntimeError("Set the OWM_API_KEY environment variable")
    owm = OWM(api_key)
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
