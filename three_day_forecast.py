#!/usr/local/bin/python
# coding: latin-1
"""
three_day_forecast.py -- Display three day weather forecast for 95051 using Weather Underground's API
"""
# MLPrince 2012 ｡◕ ‿ ◕｡ 

import urllib2
import json
from private import APIKEY

def get_forecast():
    """ 
    Makes a call to wunderground's API and displays three-day weather forecast. 
    """
    # Open url, make call to the API using an API key.
    f = urllib2.urlopen('http://api.wunderground.com/api/' + APIKEY + '/forecast/q/95051.json')
    json_string = f.read() # Save response as a json string.
    parsed_json = json.loads(json_string) # Parse the json string.

    # If there is a forecast...
    if parsed_json:

        # Extract a 3-day forecast from the parsed json (elements 2 through the end).
        three_day_forecast = parsed_json['forecast']['txt_forecast']['forecastday'][2:]
        for day in three_day_forecast:
            print day['title'], day['fcttext']

    # Otherwise...
    else:

        # Print the following string.
        print "There is no forecast.  Doom is imminent."

    # Hang up the phone.
    f.close()

def main():
    get_forecast()

if __name__ == '__main__':
    main()
