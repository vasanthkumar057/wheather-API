import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key from .env
api_key = os.getenv("wheather_apu")

# Input city
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Fetch data
response = requests.get(url)
data = response.json()

# Check if city is found
if response.status_code == 200:
    name = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']

    print(f"Weather in {name}, {country}:")
    print(f"Temperature: {temp}°C")
    print(f"Description: {description}")
    print(f"Icon code: {icon} (use this code to display weather icon if needed)")
else:
    print("City not found. Please check the name.")
