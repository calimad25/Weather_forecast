import requests
import pprint

url1 = "https://api.openweathermap.org/data/2.5/forecast?q=Madrid&appid=8ac2f887096da01213fa3db827e593d4&units=metric"
url2 = "https://api.openweathermap.org/data/2.5/forecast?lat=40.1&lon=3.4&appid=8ac2f887096da01213fa3db827e593d4&units=metric"
# r = requests.get(url1)
# print(r.json()) # below is how one item from the 'list' looks like


class Weather:

    def __init__(self, apikey, city=None, lat=None, lon=None):  # if not set to None => error if argh is not defined
        if city:  # checks if city is None => False
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()  # dictionary
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("Provide either a city or lat and lon arguments!!!")
            # replace the error message cuz print will not be shown cuz of the error

        if self.data['cod'] != "200":
            raise ValueError(self.data["message"])

    def next_12h(self):
        return self.data['list'][:4]
        # return only the first 4 items 'list' from the json dict.
        # one item contains weather data for the next 3 hours => 3x4 = 12

    def next_12h_simplified(self):
        simple_data = []
        for i in self.data['list'][:4]:
            simple_data.append((i['dt_txt'], i['main']['temp'], i['weather'][0]['description']))
            # cannot append multiple items. Only one => extract data as a tuple => append a tuple
        return simple_data  # return can only return the first data. => return the appended empty list
        # for loop needed cuz [:4] cannot work at return TypeError: list indices must be integers or slices, not str
        # i['dt_text'] = self.data['list'][0]['dt_txt']
        # if you don't use return it will automatically return a None value!


# weather = Weather(apikey="8ac2f887096da01213fa3db827e593d4", city="Rome")
# weather = Weather(apikey="8ac2f887096da01213fa3db827e593d4", lat=4.1, lon=4.5)
# weather = Weather(apikey="8ac2f887096da01213fa3db827e593d4")
weather = Weather(apikey="8ac2f887096da01213fa3db827e593d4", city="asdasd")
# print(weather.data)
pprint.pprint(weather.next_12h_simplified())



# {'clouds': {'all': 0},
#  'dt': 1673805600,
#  'dt_txt': '2023-01-15 18:00:00',
#  'main': {'feels_like': 6.01,
#           'grnd_level': 999,
#           'humidity': 46,
#           'pressure': 1018,
#           'sea_level': 1018,
#           'temp': 7.07,
#           'temp_kf': -2.19,
#           'temp_max': 9.26,
#           'temp_min': 7.07},
#  'pop': 0,
#  'sys': {'pod': 'd'},
#  'visibility': 10000,
#  'weather': [{'description': 'clear sky',
#               'icon': '01d',
#               'id': 800,
#               'main': 'Clear'}],
#  'wind': {'deg': 359, 'gust': 2.65, 'speed': 1.77}}

# ERRORS
# Traceback (most recent call last):
#   File "D:\IT\Python\Lessons\Udemy\Advanced Python Programming Build 10 OOP Aps\Lessons\
#   10_Weather_Forecast\main.py", line 73, in <module>
#     pprint.pprint(weather.next_12h_simplified())
#   File "D:\IT\Python\Lessons\Udemy\Advanced Python Programming Build 10 OOP Aps\Lessons\
#   10_Weather_Forecast\main.py", line 59, in next_12h_simplified
#     for i in self.data['list'][:4]:
# AttributeError: 'Weather' object has no attribute 'data'

# Traceback (most recent call last):
#   File "D:\IT\Python\Lessons\Udemy\Advanced Python Programming Build 10 OOP Aps\Lessons\
#   10_Weather_Forecast\main.py", line 81, in <module>
#     pprint.pprint(weather.next_12h_simplified())
#   File "D:\IT\Python\Lessons\Udemy\Advanced Python Programming Build 10 OOP Aps\Lessons\
#   10_Weather_Forecast\main.py", line 67, in next_12h_simplified
#     for i in self.data['list'][:4]:
# KeyError: 'list'

# {'cod': '404', 'message': 'city not found'}
