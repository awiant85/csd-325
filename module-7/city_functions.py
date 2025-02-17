# Austin Wiant - Assignment 7.2 - 2/16/2025

# city_functions.py

def city_country(city, country, population=None, language=None):
    """Return a formatted string of City, Country - optional population and language."""
    formatted = f"{city.title()}, {country.title()}"
    if population:
        formatted += f" - population {population}"
    if language:
        formatted += f", {language.title()}"
    return formatted

# Call the function three times with different parameters
print(city_country("santiago", "chile"))  # City, Country
print(city_country("paris", "france", 2148327))  # City, Country, Population
print(city_country("tokyo", "japan", 13929286, "japanese"))  # City, Country, Population, Language





