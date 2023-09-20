
# Initialize a list called 'travel_log' containing dictionaries with travel information
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

"""Adds new country's travel information to travel log.

    Args:
        country_visited: country visited
        times: how many times visited
        cities_visited: cities visited

    Returns: An appended version of the travel log
"""
def add_new_country(country_visited, times, cities_visited):
    # Create a new dictionary to represent the travel information for the new country
    new_country = {}
    
    # Assign values to the keys in the new_country dictionary
    new_country["country"] = country_visited
    new_country["visits"] = times
    new_country["cities"] = cities_visited

    # Append the new_country dictionary to the 'travel_log' list
    travel_log.append(new_country)

# Call the 'add_new_country' function to add travel information for a new country (Russia) to the 'travel_log'
add_new_country("Russia", 2, ["Moscow", "City", "City2"])

# Print the updated 'travel_log' list to display all travel information
print(travel_log)
