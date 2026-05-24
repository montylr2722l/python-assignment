import requests

city = input("Enter city name: ")

api_key = "8a32a0b275cada5a0050a7204378ae0c"

# units=metric se temperature Celsius me aayega
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    # Data extraction
    city_name = data["name"]
    country = data["sys"]["country"]

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]

    weather = data["weather"][0]["description"]

    wind_speed = data["wind"]["speed"]

    # Output
    print("\n------ WEATHER REPORT ------")
    print(f"City        : {city_name}")
    print(f"Country     : {country}")
    print(f"Temperature : {temperature}°C")
    print(f"Feels Like  : {feels_like}°C")
    print(f"Min Temp    : {temp_min}°C")
    print(f"Max Temp    : {temp_max}°C")
    print(f"Humidity    : {humidity}%")
    print(f"Pressure    : {pressure} hPa")
    print(f"Weather     : {weather}")
    print(f"Wind Speed  : {wind_speed} m/s")

except requests.exceptions.HTTPError:
    print("City not found or invalid API key.")

except requests.exceptions.RequestException as e:
    print("Error:", e)