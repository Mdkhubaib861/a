# import requests
# import json
# city=input(" Enter the city you are looking for: ")
# url2="https://nominatim.openstreetmap.org/search?q=kabul&format=json&limit=1"
# url1=f'''https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1'''
# r=requests.get(url2)
# print(r)
# city=input("Enter the city you are looking for: ")
# import requests
# url_latlong = f'''https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1'''
# headers = {
#     "User-Agent": "my-weather-app"
# }
# response = requests.get(url_latlong, headers=headers)
# print(response.status_code)
# data = response.json()
# print(data[0]['lat'],data[0]['lon'])
# lat=data[0]['lat']
# long=data[0]['lon']
# url_weather =f'''https://weather.googleapis.com/v1/currentConditions:lookup?location.latitude={lat}&location.longitude={long}&key=AIzaSyBkcmchhtQh8z-7tLV76T4_t9bSGxbWCWk'''
# weather_response = requests.get(url_weather, headers=headers)
# print(weather_response.status_code)
# weather_data = weather_response.json()
# print(weather_data)
#
# # # Step 3: Extract only useful info
# # temp = weather_data['temperature']['degrees']
# # humidity = weather_data['relativeHumidity']
# # condition = weather_data['weatherCondition']['description']
# # wind = weather_data['wind']['speed']['value']
# #
# # # Step 4: Print clean output
# # print(f"\nWeather in {city}:")
# # print(f"Temperature: {temp}°C")
# # print(f"Humidity: {humidity}%")
# # print(f"Condition: {condition}")
# # print(f"Wind Speed: {wind} km/h")
city=input("Enter the city you are looking for: ")
import requests
url_latlong = f'''https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1'''
headers = { "User-Agent": "my-weather-app" }
response = requests.get(url_latlong, headers=headers)
print(response.status_code)
data = response.json()
print(data[0]['lat'],data[0]['lon'])
lat=data[0]['lat']
long=data[0]['lon']
url_weather =f'''https://weather.googleapis.com/v1/currentConditions:lookup?location.latitude={lat}&location.longitude={long}&key=AIzaSyBkcmchhtQh8z-7tLV76T4_t9bSGxbWCWk'''
weather_response = requests.get(url_weather, headers=headers)
print(weather_response.status_code)
weather_data = weather_response.json()
print(weather_data)
