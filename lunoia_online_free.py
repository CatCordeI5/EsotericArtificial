import requests

class FreeWebHook:
    def __init__(self):
        self.headers = {'User-Agent': 'LunoiaAI/0.1'}

    def search_wikipedia(self, query, lang="en"):
        """Search Wikipedia"""
        try:
            lang_code = "id" if lang == "id" else "en"
            url = f"https://{lang_code}.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
            response = requests.get(url, headers=self.headers, timeout=5)
            if response.status_code == 200:
                data = response.json()
                return data.get('extract', 'No summary found.')
        except:
            return None
        return None

    def get_weather(self, city):
        """Get weather via Open-Meteo (Free)"""
        try:
            geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
            geo_res = requests.get(geo_url, timeout=5).json()
            if not geo_res['results']: return "City not found."
            
            lat = geo_res['results'][0]['latitude']
            lon = geo_res['results'][0]['longitude']
            
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            weather_res = requests.get(weather_url, timeout=5).json()
            temp = weather_res['current_weather']['temperature']
            return f"{temp}°C"
        except:
            return "Weather data unavailable."

    def process_query(self, query, lang="en"):
        """Router for free online data"""
        q_lower = query.lower()
        
        if "cuaca" in q_lower or "weather" in q_lower:
            city = q_lower.replace("cuaca", "").replace("weather", "").strip()
            if city: return f"Weather in {city}: {self.get_weather(city)}"
            
        return self.search_wikipedia(query, lang)
