import requests

# Define the URL
url = "http://159.203.121.13:8080/v1/snomed/concepts/22298006"

# Send GET request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Extract fields
effective_time = data["effectiveTime"]
active_status = data["active"]

# Print using f-strings
print(f"The concept is active: {active_status}, with effective time: {effective_time}")