import json
import os

# Step 1: Get filename input from user
filename = input("Enter the filename (e.g., data.csv): ")
loc_file = os.path.join("C:\\dataset1", filename)

# Step 2: Load JSON configuration
try:
    with open("C:\\dataset2\\dma.json", "r") as file_open_from_disk_mem:
        json_file = json.load(file_open_from_disk_mem)
except FileNotFoundError:
    print("Error: dma.json file not found in C:\\dataset2")
    exit(1)
except json.JSONDecodeError:
    print("Error: Invalid JSON format in dma.json")
    exit(1)

# Step 3: Extract values from JSON
try:
    all_cols = json_file["cols"]
    col1 = all_cols[0]
    col2 = all_cols[1]
    tabname = json_file["tablename"]
    source_user_chosen = json_file["source"]
except KeyError as e:
    print(f"Error: Missing key in JSON - {e}")
    exit(1)

# Step 4: Build SQL query
query = f"SELECT {col1}, {col2} FROM {tabname}"
print("Generated SQL Query:")
print(query)

# Step 5: Handle source field
if isinstance(source_user_chosen, list):
    source = source_user_chosen
elif isinstance(source_user_chosen, str):
    source = source_user_chosen.split(",")
else:
    source = []
    print("Warning: 'source' field is not a list or comma-separated string")

print("Source list:", source)

# Optional: Load the actual data file (if needed)
if os.path.exists(loc_file):
    print(f"Data file found at: {loc_file}")
    # You can add logic here to read/process the file
else:
    print(f"Warning: Data file not found at {loc_file}")