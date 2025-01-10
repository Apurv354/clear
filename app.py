from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simulated weather data
weather_data = {
    "New York": {"temp": 5, "condition": "Cloudy"},
    "Tokyo": {"temp": 10, "condition": "Sunny"},
    "London": {"temp": 7, "condition": "Rainy"}
}

@app.route('/')
def home():
    # Render the index.html file
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    # Get the city name from the request
    data = request.get_json()
    city = data.get('city')
    
    # Fetch weather data for the city
    weather = weather_data.get(city, {"error": "City not found"})
    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simulated weather data
weather_data = {
    "New York": {"temp": 5, "condition": "Cloudy"},
    "Tokyo": {"temp": 10, "condition": "Sunny"},
    "London": {"temp": 7, "condition": "Rainy"}
}

@app.route('/')
def home():
    # Render the index.html file
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    # Get the city name from the request
    data = request.get_json()
    city = data.get('city')
    
    # Fetch weather data for the city
    weather = weather_data.get(city, {"error": "City not found"})
    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)
