from flask import Flask, request, jsonify, send_from_directory
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather",
        params={"q": city, "appid": OPENWEATHERMAP_API_KEY, "units": "metric"}
    )

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code

    data = response.json()
    return jsonify({
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],  # Weather icon
        "humidity": data["main"]["humidity"],  # Humidity
        # Wind speed in km/h
        "wind_speed": round(data["wind"]["speed"] * 3.6, 2)
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
