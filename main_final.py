import requests
import pprint


class Weather:
    """Creates a weather object getting an apikey as input
    and either a city name or lat and lon coordinates

    Package use example

    # Create a weather object using a city name:
    # The apikey below is not guaranteed to work
    # Get your own apikey from https://openwathermap.org
    # Wait a couple of minutes for the apikey to be activated

    >>> weather1 = Weather(apikey="8ac2f887096da01213fa3db827e593d4", city="Rome")

    # Using latitude and longitude coordinates
    >>> weather2 = Weather(apikey="8ac2f887096da01213fa3db827e593d4", lat=4.1, lon=4.5)

    # Get complete weather data for the next 12 hours:
    >>> weather1.next_12h()

    # Simplified data for the next 12 hours:
    >>> weather1.next_12h_simplified()

    """
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
        """Returns 3-hour data for the next 12 hours as a dict
        """
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """Returns date and time, temperature and sky condition every 3 hours for the
            next 12 hours as a tuple
        """
        simple_data = []
        for i in self.data['list'][:4]:
            simple_data.append((i['dt_txt'], i['main']['temp'], i['weather'][0]['description']))
        return simple_data
