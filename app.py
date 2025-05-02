from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Function to fetch weather data
def get_weather_data(city):
    api_key = "1da61cab997141cab2b45252252704"  # Replace with your actual API key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={jaipur}&aqi=yes"
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    weather = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather_data = get_weather_data(city)
            if weather_data:
                weather = weather_data
            else:
                error = "Couldn't fetch weather data. Please try again."
        else:
            error = "Please enter a city name."

    return render_template('index.html', weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)
