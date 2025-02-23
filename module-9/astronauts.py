import requests
import json

# This is the URL of the API that gives us data about astronauts in space
url = "http://api.open-notify.org/astros.json"

# Make an API request to get the data
response = requests.get(url)

# Check if the API request worked by printing the status code
# (200 means success!)
print("\nAPI Status Code:", response.status_code)

# Print the raw response text from the API (no formatting)
print("\nRaw API Response:")
print(response.text)

# Now let's convert the response into JSON (a format we can easily work with)
data = response.json()

# Let's print the JSON response nicely formatted
print("\nFormatted API Response (JSON):")
formatted_json = json.dumps(data, indent=4)
print(formatted_json)

# Finally, we'll neatly print each astronaut's name and their spacecraft
print("\nCurrent Astronauts in Space:")
for astronaut in data['people']:
    print(f"{astronaut['name']} is aboard {astronaut['craft']}.")
