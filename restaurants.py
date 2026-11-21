import requests


def get_nearby_restaurants(latitude, longitude, radius):

    urls = [
        "https://overpass-api.de/api/interpreter",
        "https://overpass.kumi.systems/api/interpreter"
    ]

    radius_meters = radius * 1000

    query = f"""
    [out:json][timeout:25];

    (
      nwr["amenity"="restaurant"]
      (around:{radius_meters},{latitude},{longitude});
    );

    out center tags;
    """

    headers = {
        "User-Agent": "NearBite/1.0 (student project)"
    }

    for url in urls:

        try:
            print("\nConnecting to restaurant database...")

            response = requests.post(
                url,
                data={"data": query},
                headers=headers,
                timeout=40
            )

            response.raise_for_status()

            data = response.json()

            restaurants = []

            for place in data["elements"]:

                tags = place.get("tags", {})

                name = tags.get("name", "Unnamed Restaurant")

                if "lat" in place:
                    lat = place["lat"]
                    lon = place["lon"]
                else:
                    lat = place["center"]["lat"]
                    lon = place["center"]["lon"]

                address_parts = [
                    tags.get("addr:street"),
                    tags.get("addr:suburb"),
                    tags.get("addr:city")
                ]

                address = ", ".join(
                    part for part in address_parts if part
                )

                cuisine = tags.get("cuisine", "Not specified")

                restaurant = {
                    "name": name,
                    "latitude": lat,
                    "longitude": lon,
                    "address": address if address else "Address unavailable",
                    "cuisine": cuisine
                }

                restaurants.append(restaurant)

            return restaurants

        except (requests.exceptions.RequestException, ValueError):
            print("This server is unavailable. Trying another server...")

    print("Sorry! Unable to retrieve restaurant details right now.")
    return []