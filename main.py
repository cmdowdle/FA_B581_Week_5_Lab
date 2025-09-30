import json
from pathlib import Path

# Build the path to the student.json file
data_dir = Path(__file__).parent / "data"
json_file = data_dir / "student.json"

# Open and read the JSON file
with open(json_file, "r") as file:
    data = json.load(file)

# Display the contents
print(data)

# Access individual elements
print("Name:", data["name"])
print("Age:", data["age"])
print("Courses:", data["courses"])
print("First course:", data["courses"][0])