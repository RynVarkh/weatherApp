import requests

def get_weather(city):
    # Step 1: Get latitude and longitude for the city
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_response = requests.get(geo_url).json()

    if "results" not in geo_response:
        return f"City '{city}' not found."

    lat = geo_response["results"][0]["latitude"]
    lon = geo_response["results"][0]["longitude"]
    con = geo_response["results"][0]["country"]
    pop = geo_response["results"][0]["population"]
    # Step 2: Get weather using coordinates
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
        f"&current_weather=true&daily=temperature_2m_max,temperature_2m_min"
        f"&timezone=auto"
    )
    weather_response = requests.get(weather_url).json()

    current = weather_response["current_weather"]
    daily = weather_response["daily"]

    # Step 3: Format output
    result = f"""
    Weather for {city.title()}, {con}:
    Approx City Populatin: {pop}:
    🌡 Current: {current['temperature']}°C, Wind {current['windspeed']} km/h
    📅 Today: {daily['temperature_2m_min'][0]}°C – {daily['temperature_2m_max'][0]}°C
    """
    return result

# Example usage:
print("\n---------WEATHER APP---------")
city = input("City: ")
print(get_weather(city))
