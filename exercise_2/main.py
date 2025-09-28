import json
from pathlib import Path

# 1) Build or modify your patient dict BEFORE saving
patient = {
    "patient_id": "P-0001",
    "name": "Bo Champ",
    "age": 7,
    "conditions": ["asthma", "chronic cough"],
    "is_active": True,
    "appointments": [
        {"date": "2025-12-25", "department": "Plastics", "provider": "Dr. Smith"},
        {"date": "2025-12-10", "department": "Infectious Disease", "provider": "Dr. Patel"}
    ],
    "contact": {"phone": "555-0101", "email": "jane.doe@example.com"}
}

# >>> IMPORTANT: Edit fields above with synthetic information (name, age, conditions, dates, etc.) before you run the code.

# 2) Use pathlib to point to exercise_2/data/patient.json
data_dir = Path(__file__).parent / "data"
json_path = data_dir / "patient.json"

# 3) Ensure the data directory exists
data_dir.mkdir(parents=True, exist_ok=True)

# 4) Convert dict to JSON and save with indentation
with json_path.open("w", encoding="utf-8") as f:
    json.dump(patient, f, ensure_ascii=False, indent=2)

print(f"Saved patient JSON to: {json_path.resolve()}")

# 5) (Optional) Read it back to verify
with json_path.open("r", encoding="utf-8") as f:
    loaded = json.load(f)

print("Loaded back from JSON:", loaded)