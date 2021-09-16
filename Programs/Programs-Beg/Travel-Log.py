
travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, times, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times
    new_country["cities"] = cities_visited

    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "City", "City2"])
print(travel_log)