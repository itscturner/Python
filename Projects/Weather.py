
import datetime
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}@appid={api_key}&units=metric" #imperial
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        return temperature, weather_description
    else:
        return None, None

def main():
    city_name = input("Enter City Name: ")
    api_key = input("Enter Your OpenWeatherMap API Key: ")
    
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    temperature, weather_description = get_weather(city_name, api_key)
    
    if temperature is not None and weather_description is not None:
        print(f"Current Time: {current_time}")
        print(f"Weather In {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("Failed To Retrieve Weather Information. Please Check The City Name And API Key.")

if __name__ == "__main__":
    main()
