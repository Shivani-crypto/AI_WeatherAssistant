import requests

API_KEY = 'a10b819ecb7ea21721d729384004c064'

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    return f"{city} weather: {temp}°C, {desc}"
