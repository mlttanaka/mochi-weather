#!/usr/bin/env python3
# coding: utf-8
"""
three_day_forecast.py -- Display three day weather forecast from Weather Underground.
"""
# MLT-Tanaka 2015 ｡◕ ‿ ◕｡ 

import urllib.request
import json
from private import APIKEY

def valid_zipcode(zip_code):
    # Loosely validates a zip code.
    return(zip_code.isdigit() and len(zip_code) == 5)


def get_forecast(zip_code):
    """ 
    Makes a call to wunderground's API and displays three-day weather forecast. 
    """

    url = 'http://api.wunderground.com/api/' + APIKEY + '/forecast/q/' + zip_code + '.json'
    with urllib.request.urlopen(url) as response:
        results = response.read() # Save response as a json string.

    data = json.loads(results.decode('utf-8')) # Parse the json string.

    # If there is data, print a 3-day forecast.  Otherwise, doom is emminent.
    if data:
        three_day_forecast = data['forecast']['txt_forecast']['forecastday'][2:]
        for day in three_day_forecast:
            print(day['title'], day['fcttext'])
    else:
        print("There is no weather forecast for zip code" + zip_code + "; doom is imminent.")


def main():
    zip_code = input("Enter 5-digit zip code: ")
    if valid_zipcode(zip_code):
        get_forecast(zip_code)
    else:
        print("Oddly, there is no weather forecast for zip code: " + zip_code)
        print("Doom is imminent.")


if __name__ == '__main__':
    main()
