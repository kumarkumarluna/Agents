def get_weather(city):
    weather_data = {
        "chennai": "32°C, sunny",
        "bangalore": "24°C, cloudy",
        "mumbai": "29°C, humid",
        "delhi": "31°C, clear"
    }

    return weather_data.get(
        city.lower(),
        f"Weather data unavailable for {city}"
    )