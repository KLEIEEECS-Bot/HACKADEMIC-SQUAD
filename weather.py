import requests
import os

def get_weather_multiplier(city="Dharwad"):
    API_KEY = os.getenv("WEATHER_API_KEY", "your_openweathermap_key")
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(URL)
        data = response.json()
        weather = data['weather'][0]['main']

        if weather in ["Rain", "Thunderstorm"]:
            return 1.3
        elif weather in ["Snow"]:
            return 1.2
        else:
            return 1.0
    except:
        return 1.0
