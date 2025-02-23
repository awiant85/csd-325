import requests
import json

# Star Wars API endpoint for information about Luke Skywalker
url = "https://swapi.dev/api/people/1/"

# Make an API request
response = requests.get(url)

# Check the status of the API request
print("API Status Code:", response.status_code)

# Print raw API response (unformatted)
print("\nRaw API Response:")
print(response.text)

# Convert the response into JSON format
data = response.json()

# Nicely format and print the JSON response
print("\nFormatted API Response (JSON):")
formatted_json = json.dumps(data, indent=4)
print(formatted_json)

# Extract and print specific information clearly
print("\nStar Wars Character Details:")
print("Name:", data["name"])
print("Height:", data["height"], "cm")
print("Mass:", data["mass"], "kg")
print("Hair Color:", data["hair_color"])
print("Eye Color:", data["eye_color"])
print("Birth Year:", data["birth_year"])
print("Gender:", data["gender"])
