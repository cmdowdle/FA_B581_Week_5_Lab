import requests

# Define the URL
url = "http://159.203.121.13:8080/v1/snomed/concepts/13645005/properties?expand=0&format=syn"

# Send GET request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Extract attributes for the concept (key "2")
attributes = data["2"]

# Extract "Is a" relationships for the concept (key "0")
isa_relationships = data["0"]["Is a"]

# Print using f-strings
print("Attributes:")
for key, value in attributes.items():
    print(f" - {key}: {value}")

print("\n'Is a' Relationships:")
for rel in isa_relationships:
    print(f" - {rel}")