import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Fetch API key from environment
API_KEY = os.getenv("API_KEY")
CITY = "Cleveland"

# OpenWeatherMap API endpoint
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Function to fetch weather data
def fetch_weather():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        print("✅ Weather in", CITY)
        print("🌡️ Temperature:", data['main']['temp'], "°C")
        print("🌤️ Condition:", data['weather'][0]['description'])
    else:
        print("❌ Failed to fetch weather data:", response.status_code)

# Run the function
if __name__ == "__main__":
    fetch_weather()
