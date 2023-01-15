import requests

url = "https://api.openweathermap.org/data/2.5/forecast?q=Madrid&appid=8ac2f887096da01213fa3db827e593d4&units=metric"
r = requests.get(url)
print(r.json())

class Weather:

    def __init__(self, apikey, city, lon, lat):
        pass

    def next_12h(self):
        pass

    def next_12h_simplified(self):
        pass

