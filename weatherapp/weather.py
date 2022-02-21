# weather.py
import argparse
import json
import sys
import datetime
from configparser import ConfigParser
from urllib import error, parse, request

BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
PADDING = 20
# Weather Condition Codes
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
THUNDERSTORM = range(200, 300)
DRIZZLE = range(300, 400)
RAIN = range(500, 600)
SNOW = range(600, 700)
ATMOSPHERE = range(700, 800)
CLEAR = range(800, 801)
CLOUDY = range(801, 900)

dt = datetime.datetime.fromtimestamp(0)

def read_user_cli_args():
    """ Handles the CLI user interactions.
    Returns:
        argparse.Namespace: Populated namespace object
        """
    parser = argparse.ArgumentParser(description="gets weather and temperature information for a city")
    parser.add_argument(
        "city", nargs="+", type=str, help="enter the city name"
    )
    parser.add_argument(
        "-i",
        "--imperial",
        action="store_true",
        help="display the temperature in imperial units"
    )
    return parser.parse_args()


def build_weather_query(city_input, imperial=False):
    """Builds the URL for an API request to OpenWeather's weather API.

       Args:
           city_input (List[str]): Name of a city as collected by argparse
           imperial (bool): Whether or not to use imperial units for temperature

       Returns:
           str: URL formatted for a call to OpenWeather's city name endpoint
       """
    api_key = _get_api_key()
    city_name = " ".join(city_input)
    url_encoded_city_name=parse.quote_plus(city_name)
    units = "imperial" if imperial else "metric"
    url = (
        f"{BASE_WEATHER_API_URL}?q={url_encoded_city_name}"
        f"&units={units}&appid={api_key}"
    )
    return url


def _get_api_key():
    """ Fetch the API key from you configuration file-

    Expects a configuration file named "secrets.ini" with structure:

    [openweather]
    api_key=<YOUR-OPENWEATHER-API-KEY>"""

    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]

def get_weather_data(query_url):
    """Makes an API request to a URL and returns the data as a Python object.

        Args:
            query_url (str): URL formatted for OpenWeather's city name endpoint

        Returns:
            dict: Weather information for a specific city
        """
    try:
        response = request.urlopen(query_url)
    except error.HTTPError as http_error:
        if http_error.code == 401:  # 401 - Unauthorized
            sys.exit("Access denied. Check your API key.")
        elif http_error.code == 404:  # 404 - Not Found
            sys.exit("Can't find weather data for this city.")
        else:
            sys.exit(f"Something went wrong... ({http_error.code})")

    data = response.read()

    try:
        return json.loads(data)
    except json.JSONDecodeError:
        sys.exit("Couldn't read the server response.")

def _select_weather_display_params(weather_id):
    if weather_id in THUNDERSTORM:
        display_params = ("💥")
    elif weather_id in DRIZZLE:
        display_params = ("💧")
    elif weather_id in RAIN:
        display_params = ("💦")
    elif weather_id in SNOW:
        display_params = ("⛄")
    elif weather_id in ATMOSPHERE:
        display_params = ("🌀")
    elif weather_id in CLEAR:
        display_params = ("🔆")
    elif weather_id in CLOUDY:
        display_params = ("💨")
    else:  # In case the API adds new weather codes
        display_params = ("🌈")
    return display_params

def display_weather_info(weather_Data, imperial='False'):
    """Prints formatted weather information about a city.

    Args:
        weather_data (dict): API response from OpenWeather by city name
        imperial (bool): Whether or not to use imperial units for temperature

    More information at https://openweathermap.org/current#name
    """
    city = weather_data['name']
    weather_id = weather_data['weather'][0]['id']
    weather_description = weather_data['weather'][0]['description']
    if weather_description == 'clear sky':
        weather_description = 'Cielo despejado'
    elif weather_description == 'few clouds':
        weather_description = 'Algunas nubes'
    temperature = weather_data['main']['temp']
    Tsensation = weather_data['main']['feels_like']
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    sunrise_unix = weather_data['sys']['sunrise']
    sunrise = datetime.datetime.utcfromtimestamp((sunrise_unix)).strftime(' %H:%M:%S')
    sunset_unix = weather_data['sys']['sunset']
    sunset = datetime.datetime.utcfromtimestamp((sunset_unix)).strftime(' %H:%M:%S')


    print(f"{city}", end="  ")
    #weather_symbol = _select_weather_display_params(weather_id)
    #print(f"\t{weather_symbol}", end=" ")
    print(f"{weather_description.capitalize()}", end="  ")
    print(f"(Temperatura:{temperature:}º{'F' if imperial else 'C':})", end="  ")
    print(f"(Sensación:{Tsensation}º{'F' if imperial else 'C'})", end="  ")
    print(f"{pressure}bar", end="  ")
    print(f"{humidity}%", )
    print(f"Amanece:{sunrise}", end="  ")
    print(f"Anochece: {sunset}")


if __name__  == "__main__":
    user_args = read_user_cli_args()
    query_url = build_weather_query(user_args.city, user_args.imperial)
    weather_data = get_weather_data(query_url)
    display_weather_info(weather_data, user_args.imperial)


