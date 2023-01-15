import requests

url = "https://api.openweathermap.org/data/2.5/forecast?q=Madrid&appid=8ac2f887096da01213fa3db827e593d4&units=metric"
r = requests.get(url)
print(r.json())

class Weather:

    def __init__(self, apikey, city, lon=None, lat=None):
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric"
        r = requests.get(url)
        self.data = r.json()

    def next_12h(self):
        return self.data

    def next_12h_simplified(self):
        pass


weather = Weather(apikey="8ac2f887096da01213fa3db827e593d4", city="Rome")
print(weather.data)
print(weather.next_12h())
