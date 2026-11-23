from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()



def get_weather(place):
    observation = mgr.weather_at_place(place)
    w = observation.weather
    weather = (
        f"Weather descriptions: {w.detailed_status}\n"
        f"Wind: {w.wind()["speed"]} m/s\n"
        f"Temperature: {w.temperature('celsius')['temp']}°C\n"
        f"Rain: {w.rain}\n"
        f"Heat index: {w.heat_index}\n"
        f"Clouds: {w.clouds}\n"
    )
    return weather


if __name__ == "__main__":
    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place('London,GB')
    w = observation.weather
    print(w.detailed_status)         # 'clouds'
    print(w.wind())                  # {'speed': 4.6, 'deg': 330}
    print(w.humidity)                # 87
    print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    print(w.rain)                    # {}
    print(w.heat_index)              # None
    print(w.clouds)                  # 75





