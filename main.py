from location import get_coordinates
from restaurants import get_nearby_restaurants
from distance import calculate_distance


def welcome():
    print("\n" + "=" * 45)
    print("                 NEARBITE")
    print("          Find food. Stay in budget.")
    print("=" * 45)


def get_user_preferences():

    location = input("\nEnter your location: ").strip()

    while not location:
        print("Location cannot be empty.")
        location = input("Enter your location: ").strip()

    print("\nSelect your budget:")
    print("1. Under Rs. 150")
    print("2. Rs. 150 - Rs. 300")
    print("3. Rs. 300 - Rs. 500")
    print("4. No budget preference")

    budget_options = {"1": "Under Rs. 150","2": "Rs. 150 - Rs. 300","3": "Rs. 300 - Rs. 500",
        "4": "No budget preference"}

    budget = input("\nEnter your choice (1-4): ")

    while budget not in budget_options:
        print("Invalid choice! Please select between 1 and 4.")
        budget = input("Enter your choice (1-4): ")

    while True:
        try:
            radius = float(input("\nEnter search radius (in km): "))

            if radius <= 0:
                print("Radius must be greater than zero.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    return location, budget_options[budget], radius


def main():

    welcome()

    location, budget, radius = get_user_preferences()

    print("\nFinding your location...")

    coordinates = get_coordinates(location)

    if coordinates is None:
        return

    latitude, longitude = coordinates

    print("\nSearching for nearby restaurants...")

    restaurants = get_nearby_restaurants(latitude, longitude, radius)

    if not restaurants:
        print("No restaurants found. Try another location or radius.")
        return

    for restaurant in restaurants:

        restaurant["distance"] = calculate_distance(latitude,longitude,
            restaurant["latitude"],
            restaurant["longitude"])

    restaurants.sort(key=lambda item: item["distance"])

    print("\n" + "=" * 55)
    print("             NEARBY RESTAURANTS")
    print("=" * 55)

    for number, restaurant in enumerate(restaurants[:10], start=1):

        print(f"\n{number}. {restaurant['name']}")
        print("   Address:", restaurant["address"])
        print("   Cuisine:", restaurant["cuisine"])
        print("   Distance:", restaurant["distance"], "km")

    print("\n" + "=" * 55)
    print("        Thank you for using NearBite!")
    print("=" * 55)


if __name__ == "__main__":
    main()