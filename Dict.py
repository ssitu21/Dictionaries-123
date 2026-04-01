# Create a nested dictionary for cities
cities = {
    "Tokyo": {
        "country": "Japan",
        "population": "37 million",
        "fact": "Tokyo is the largest metropolitan area in the world.",
    },
    "Paris": {
        "country": "France",
        "population": "2.1 million",
        "fact": "Paris is known as the 'City of Light'.",
    },
    "New York": {
        "country": "USA",
        "population": "8.4 million",
        "fact": "New York City is home to the Statue of Liberty.",
    },
}

# Loop through the cities dictionary and print neatly
for city_name, city_info in cities.items():
    print(f"\nCity: {city_name}")
    print(f"\tCountry: {city_info['country']}")
    print(f"\tPopulation: {city_info['population']}")
    print(f"\tFact: {city_info['fact']}")
