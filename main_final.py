import requests
import pprint


class Weather:

    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("Provide either a city or lat and lon arguments!!!")

        if self.data['cod'] != "200":
            raise ValueError(self.data["message"])

    def next_12h(self):
        return self.data['list'][:4]

    def next_12h_simplified(self):
        simple_data = []
        for i in self.data['list'][:4]:
            simple_data.append((i['dt_txt'], i['main']['temp'], i['weather'][0]['description']))
        return simple_data


# weather = Weather(apikey="8ac2f887096da01213fa3db827e593d4", city="Rome")
# weather = Weather(apikey="8ac2f887096da01213fa3db827e593d4", lat=4.1, lon=4.5)
# weather = Weather(apikey="8ac2f887096da01213fa3db827e593d4")
weather = Weather(apikey="8ac2f887096da01213fa3db827e593d4", city="asdasd")
# print(weather.data)
pprint.pprint(weather.next_12h_simplified())
