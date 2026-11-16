from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather(location):

    observation = mgr.weather_at_place(location)
    return observation.weather


def format_weather(weather):

    result = (
        f"Weather: {weather.detailed_status}\n"
        f"Wind speed: {weather.wind()['speed']} m/s\n"
        f"Wind direction: {weather.wind().get('deg', 'N/A')}°\n"
        f"Humidity: {weather.humidity}%\n"
        f"Temperature: {weather.temperature('celsius')['temp']} °C\n"
        f"Rain in last 1H: {str(weather.rain.get('1h', 0)) + " mm"}\n"
        f"Cloudiness: {weather.clouds}%\n"
        f"Pressure: {weather.pressure['press']} hPa"
    )

    return result
    

if __name__ == "__main__":

    location = "Kyiv,UA"
    w = get_weather(location)
    
    # print(w.detailed_status)         # 'clouds'
    # print(w.wind())                  # {'speed': 4.6, 'deg': 330}
    # print(w.humidity)                # 87
    # print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    #print(w.rain)                    # {}
    #print(w.pressure)                 # {'press': 1028, 'sea_level': 1028} hPa
    # print(w.clouds)                  # 75

    print(format_weather(w))
