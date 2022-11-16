#!/usr/bin/env python3

"""Return the  location of the ISS in lon/lat"""
import requests

URL = "http://api.open-notify.org/iss-now.json"
def main():
    resp = requests.get(URL).json

    lat = resp ["iss_position"]["latitude"]
    lon = resp ["iss_position"]["longitude"]

    print(f"""
    Exact LOCATION OF THE ISS AT THIS MOMENT IS:
    Lat: {lat}
    Lon: {lon}
    """)

    if __name__ == "__main__":
        main()


