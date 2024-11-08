# openweather api key ba3cf7d1ee5d606e4fc95bea62f38484
# news api key : 4db04140af7d463597faf62bd6f2c5b3
import requests

class DataRetriever:
    def __init__(self, api_url="https://en.wikipedia.org/api/rest_v1/page/summary/"):
        self.api_url = api_url

    def fetch_data(self, query):
        # Daha doğru API yanıtları için sorguyu işleyelim
        try:
            query = query.strip().replace(" ", "_")  # Sorgu formatını düzeltiyoruz.
            response = requests.get(self.api_url + query)
            response.raise_for_status()  # HTTP hatası kontrolü
            data = response.json()
            # Eğer extract varsa, döneceğiz
            return data.get("extract", "No relevant information found.")
        except requests.exceptions.RequestException as e:
            return f"Error fetching data from Wikipedia: {str(e)}"
