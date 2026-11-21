import requests


def get_coordinates(location):

    url = "https://nominatim.openstreetmap.org/search"

    params = {"q": location,"format": "jsonv2","limit": 1,
        "countrycodes": "in"}

    headers = {"User-Agent": "NearBite/1.0 (student project)"}

    try:
        response = requests.get(url,params=params,
            headers=headers,
            timeout=10)

        response.raise_for_status()

        results = response.json()

        if not results:
            print("Sorry! Location not found.")
            return None

        latitude = float(results[0]["lat"])
        longitude = float(results[0]["lon"])

        return latitude, longitude

    except requests.exceptions.RequestException:
        print("Unable to connect to the location service.")
        return None

    except (ValueError, KeyError, IndexError):
        print("Unable to process the location details.")
        return None