import requests

api_key = '483211754a40bea28edb022818fa98f0'

baseURL = "http://api.openweathermap.org/data/2.5/weather?"
userCity = input("Select city: ")

def kelvin_conversion(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = baseURL + "appid=" + api_key + "&q=" + userCity
response = requests.get(url).json()

temp_kelvin = response ['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_conversion(temp_kelvin) 
feel_kelvin =  response ['main']['feels_like']
feel_celsius, feel_fahrenheit = kelvin_conversion(feel_kelvin)
humidity = response ['main']['humidity']
wind_speed = response ['wind']['speed']
description = response ['weather'][0]['description']

print(f"Temperature in {userCity}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
print(f"Temperature in {userCity} feels like: {feel_celsius:.2f}°C or {feel_fahrenheit:.2f}°F")
print(f"Humidity in {userCity}: {humidity}%")
print(f"Wind speed in {userCity}: {wind_speed} m/s")
print(f"General weather in {userCity}: {description}")