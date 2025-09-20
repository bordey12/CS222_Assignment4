import json
import ssl
from urllib.request import urlopen

def main():
    url = "https://api.weather.gov/points/40.1934,-85.3864"
    context = ssl._create_unverified_context()
    response = urlopen(url, context=context)
    weather_data = json.loads(response.read())

    secondURL = weather_data['properties']['forecast']
    response = urlopen(secondURL, context=context)
    forecast_data = json.loads(response.read())

    for time in forecast_data['properties']['periods']:
        print(time.get('name'), "will be", time.get('temperature'), "degrees. " "Details: ", time.get('detailedForecast'))

if __name__ == "__main__":
    main()