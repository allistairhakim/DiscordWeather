from pypresence import Presence
import time
import requests, json

CITY = 'London'
COUNTRY_CODE = 'UK'
API_KEY = 'AAAAA' #Fake OpenWeatherMap API key insert your own
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
UNIT_SYSTEM = 'imperial'
URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY + "&units=" + UNIT_SYSTEM

CLIENT_ID = '829867475720994826'

def GetWeather():
    response = requests.get(URL)
    data = response.json()
    if data['cod'] != 404:
        weather_description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp_min']
        wind = data['wind']['speed']
        humidity = data['main']['humidity']
        return [weather_description, str(temp), icon, str(wind), str(humidity)]
    else:
        return None

if __name__ == '__main__':
    RPC = Presence(CLIENT_ID)
    RPC.connect()

    while True:
        data = GetWeather()
        print(RPC.update(state=data[0], details=data[1] + '°F', large_image=data[2], buttons = [{'label':'Wind 💨: ' + data[3] + ' mph', 'url': 'https://github.com/allistairhakim'}, {'label': 'Humidity 🌧️: ' + data[4] + '%', 'url': 'https://github.com/allistairhakim' }]))
        HALF_HOUR = 60 * 30
        time.sleep(HALF_HOUR)
