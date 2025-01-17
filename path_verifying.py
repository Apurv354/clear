import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the full path to 1.json
json_path = os.path.join(current_dir, "client_secret_734108785104-i3kcdvo7fhq30isoam691620kpgnbif7.apps.googleusercontent.com.json")

# Open and read the JSON file
with open(json_path, "r") as file:
    data = file.read()
    print(data)