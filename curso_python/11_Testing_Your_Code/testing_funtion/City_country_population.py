"""
11-2. Population: Modify your function so it requires a third parameter,
population. It should now return a single string of the form City, Country –
population xxx, such as Santiago, Chile – population 5000000. Run test
_cities.py again. Make sure test_city_country() fails this time.
Modify the function so the population parameter is optional. Run test
_cities.py again, and make sure test_city_country() passes again.
Write a second test called test_city_country_population() that verifies
you can call your function with the values 'santiago', 'chile', and
'population=5000000'. Run test_cities.py again, and make sure this new test
passes.
"""

def City_Country_Population_funtions(city, country, population = 0 ):

    if population:
        formatted_name = f"{city} {country} Population: {population}"
    else:
        formatted_name = f"{city} {country}"
    return formatted_name.title()


def City_Country_Population_funtions_2(city, country, population = 0 ):

    formatted_name = f"{city} {country}"
    if population:
        formatted_name += f" Population: {population}"
    return formatted_name.title()
