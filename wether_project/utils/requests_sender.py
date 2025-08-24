import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timezone
from geopy.geocoders import Nominatim
from utils.csv_reader import read_city_names




class WeatherFetcher:
    def __init__(self):
        self.username = 'miniroc_mueller_daniel'
        self.password = 'HPq667K7WH2IsoX968ks'
        self.parameter = "t_2m:C"
        self.geolocator = Nominatim(user_agent="weather_app")

    def get_weather(self, city_name: str):
        location = self.geolocator.geocode(city_name)
        if not location:
            return f"{city_name}: не удалось найти координаты"

        lat, lon = location.latitude, location.longitude
        date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        url = f"https://api.meteomatics.com/{date}/{self.parameter}/{lat},{lon}/json"

        response = requests.get(url, auth=HTTPBasicAuth(self.username, self.password), timeout=10)

        if response.status_code == 200:
            data = response.json()
            temp = data["data"][0]["coordinates"][0]["dates"][0]["value"]
            return f"{city_name}: {temp}°C"
        else:
            return f"{city_name}: Ошибка {response.status_code}"

    def get_weather_from_csv(self, filename=r"utils\cities.csv"):
        cities = read_city_names(filename)
        results = []
        for city in cities:
            results.append(self.get_weather(city))
        return results

