# Assignment 6.11
# Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a
#         dictionary of information about each city and include the country that the city is in, its approximate
#         population, and one fact about that city. The keys for each city’s dictionary should be something like
#         country, population, and fact. Print the name of each city and all of the information you have stored about it.

print("Try-it-Yourself:")
print("Assignment 6.11")

cities = {
    "cleveland": {
        "country": "united states",
        "population": 383_331,
        "fact": "Home of the Rock & Roll Hall of Fame"
    },
    "london": {
        "country": "england",
        "population": 8_982_000,
        "fact": "Hosted the 2012 Summer Olympics"
    },
    "ensenada": {
        "country": "mexico",
        "population": 443_807,
        "fact": "Known as the 'Capital del vino Mexicano' (Capital of Mexican wine)"
    },
}

for city, facts in cities.items():
    print(f"\n{city.title()}")
    for heading, fact in cities[city].items():
        if heading == "country":
            fact = fact.title()
        print(f"\t{heading.upper()}:\n\t\t{fact}")
