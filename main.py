import requests

city = input("Enter city with country: ")
url = f"http://api.weatherapi.com/v1/current.json?key=99b32e47aa574768a0f173331240404&q={city}&aqi=no"

response = requests.get(url).json()
print("Region:",response["location"]["region"])
print("Country:",response["location"]["country"])
print("Local Time:",response["location"]["localtime"])
print("Current Temperature in Celcius:",response["current"]["temp_c"])
print("Current Condition:",response["current"]["condition"]["text"])
print("Current Wind Speed in KPH:",response["current"]["wind_kph"])
print("Wind Direction:",response["current"]["wind_dir"])
print("Current Humidity:",response["current"]["humidity"])
