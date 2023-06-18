import argparse
import pyfiglet
from simple_chalk import chalk
import requests

# API key for openweathmap

API_KEY= "4fdb388dd42af6ce4ab4e9ffc95a7b95"

#Base URL from openweathermap

BASE_URL="https://api.openweathermap.org/data/2.5/weather"

#Map the weather codes to weather icons

WEATHER_ICONS={
    "01d": "clear sky day",
    "02d": "few clouds day"

}

#construct API URL with query parameters
parser=argparse.ArgumentParser(description="Check the weather for a certain country/city")
parser.add_argument("country", help="The country/city to check the weather for")
args=parser.parse_args()
url= f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"

#Make API request and parse response using requests module
response= requests.get(url)
if response.status_code!=200:
    print(chalk.red("Error: Unable to retrie e weather information"))
    exit()
# Parsing the JSON response from the ApI and extract the weather information
data=response.json()

# Get information from response
temperature =data["main"]["temp"]
feels_like=data['main']["feels_like"]
description=data["weather"][0]["description"]
icon=data["weather"][0]["icon"]
city=data["name"]
country=data["sys"]["country"]

#construct the output with weather icons
output=""
weather_icon=WEATHER_ICONS.get(icon,"")
output+=f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output+=f"{weather_icon}{description}\n"
output+=f"Temperature: {temperature}C \n"
output+=f"Fell like: {feels_like}C\n"

print(chalk.green(output))
