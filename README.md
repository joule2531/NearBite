# NearBite 🍽️

### Find food. Stay in budget.

NearBite is a small Python project I developed to make finding nearby restaurants a little easier.

The idea behind this project was simple: sometimes we want to find a place to eat nearby without spending too much time searching through different apps and websites.

With NearBite, users can enter their location, choose a budget preference and set how far they are willing to search. The program then finds nearby restaurants and displays the 10 closest ones, along with their distance, address and cuisine information wherever available.

## What can NearBite do?

- Search for restaurants based on the location entered by the user.
- Allow users to select a preferred budget range.
- Let users choose their search radius.
- Find nearby restaurants using OpenStreetMap data.
- Calculate the distance between the user's location and each restaurant.
- Arrange the results from nearest to farthest.
- Display up to 10 nearby restaurants.
- Try another server if the first one is temporarily unavailable.

## Technologies Used

Here are the tools and technologies I used to build this project:

- **Python** – For developing the application.
- **Requests** – To send requests and retrieve data from online services.
- **OpenStreetMap** – For restaurant and location data.
- **Nominatim** – To convert place names into geographical coordinates.
- **Overpass API** – To retrieve nearby restaurant information.
- **Math module** – To calculate distances using the Haversine formula.

## Project Structure

```text
NEARBITE/
│
├── main.py
├── location.py
├── restaurants.py
├── distance.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

## How to Run the Project

Follow these steps to run NearBite on your computer.

**1. Clone the repository**

```bash
git clone https://github.com/joule2531/NearBite.git
```

**2. Open the project folder**

```bash
cd NEARBITE
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

For Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

**5. Install the required packages**

```bash
pip install -r requirements.txt
```

**6. Run NearBite**

```bash
python main.py
```

## How Does It Work?

The working of NearBite is quite simple:

1. The user enters a location.
2. Nominatim finds the latitude and longitude of that location.
3. The Overpass API searches for restaurants within the selected radius.
4. The program calculates the distance to each restaurant using the Haversine formula.
5. The restaurants are sorted based on distance.
6. Finally, the 10 closest results are displayed.

## A Few Limitations

While building this project, I also came across a few limitations:

- The results depend on the information available in OpenStreetMap.
- Ratings and review counts are not currently available.
- Restaurant prices are not reliably available, so budget-based filtering is not yet implemented.
- Some restaurants may not have complete address or cuisine details.
- The public Overpass servers may occasionally be unavailable.

## Future Improvements

There are still a few things I'd like to improve in NearBite:

- Add more reliable restaurant price information.
- Include ratings and reviews.
- Improve the overall user interface.
- Add more options to filter restaurant results.

## Acknowledgements

NearBite uses data from [OpenStreetMap](https://www.openstreetmap.org/). Restaurant information is retrieved using the Overpass API, and location search is handled through Nominatim.

Map data © OpenStreetMap contributors.

## License

This project is licensed under the MIT License.