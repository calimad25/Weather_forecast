import requests

url1 = "https://api.openweathermap.org/data/2.5/forecast?q=Madrid&appid=8ac2f887096da01213fa3db827e593d4&units=metric"
url2 = "https://api.openweathermap.org/data/2.5/forecast?lat=40.1&lon=3.4&appid=8ac2f887096da01213fa3db827e593d4&units=metric"
# r = requests.get(url1)
# print(r.json())


class Weather:

    def __init__(self, apikey, city=None, lat=None, lon=None):  # if not set to None => error if argh is not defined
        if city:  # checks if city is None => False
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        else:
            print("Provide either a city or lat and lon arguments")

    def next_12h(self):
        return self.data

    def next_12h_simplified(self):
        pass


# weather = Weather(apikey="8ac2f887096da01213fa3db827e593d4", city="Rome")
weather = Weather(apikey="8ac2f887096da01213fa3db827e593d4", lat=4.1, lon=4.5)
# print(weather.data)
print(weather.next_12h())
