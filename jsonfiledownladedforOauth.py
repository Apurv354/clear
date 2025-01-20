import json

# Specify the file name
json_file = "client_secret_734108785104-i3kcdvo7fhq30isoam691620kpgnbif7.apps.googleusercontent.com.json"  # Assumes the script and 1.json are in the same folder

# Open and load the JSON file
with open(json_file, "r") as file:
    data = json.load(file)  # Load JSON as a Python dictionary

# Print the data
print("JSON content:")
print(json.dumps(data, indent=4))  # Pretty-print the JSON


