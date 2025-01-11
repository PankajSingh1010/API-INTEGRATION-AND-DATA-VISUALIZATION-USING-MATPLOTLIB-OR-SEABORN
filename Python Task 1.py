import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# 1. Fetch Data from OpenWeatherMap API
api_key = "bed5cdbe6e772aeeebb11d17c489d253"  # Your API Key
city = "Kolkata"  # You can change this to any city of your choice
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)

# Check if the response is valid
if response.status_code == 200:
    data = response.json()
    print("API call successful! Here's a sample of the data:", data)
else:
    print(f"API call failed with status code {response.status_code}")
    exit()

# 2. Process and Convert Data
temperature_kelvin = data['main']['temp']
feels_like_kelvin = data['main']['feels_like']
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']
cloud_coverage = data['clouds']['all']
visibility = data['visibility']
weather_description = data['weather'][0]['description']
sunrise_timestamp = data['sys']['sunrise']
sunset_timestamp = data['sys']['sunset']

# Convert temperature from Kelvin to Celsius
temperature_celsius = temperature_kelvin - 273.15
feels_like_celsius = feels_like_kelvin - 273.15

# Convert timestamps to human-readable time (sunrise and sunset)
sunrise_time = datetime.utcfromtimestamp(sunrise_timestamp).strftime('%H:%M:%S')
sunset_time = datetime.utcfromtimestamp(sunset_timestamp).strftime('%H:%M:%S')

# 3. Visualization

# Prepare data for plotting
labels = ['Temperature (°C)', 'Feels Like (°C)', 'Humidity (%)', 'Wind Speed (m/s)', 'Cloud Coverage (%)', 'Visibility (m)', 'Weather Description', 'Sunrise', 'Sunset']
values = [temperature_celsius, feels_like_celsius, humidity, wind_speed, cloud_coverage, visibility, weather_description, sunrise_time, sunset_time]

# Set up the figure with a larger size
fig, axes = plt.subplots(3, 3, figsize=(18, 16))
fig.tight_layout(pad=5.0)

# Plot each value with custom titles and formats
axes[0, 0].barh(['Temperature (°C)'], [temperature_celsius], color='skyblue')
axes[0, 0].set_title(f"Location: {city} - Temperature: {temperature_celsius:.2f}°C")
axes[0, 0].set_yticklabels([''])  # Remove horizontal label

axes[0, 1].barh(['Feels Like (°C)'], [feels_like_celsius], color='salmon')
axes[0, 1].set_title(f"Location: {city} - Feels Like: {feels_like_celsius:.2f}°C")
axes[0, 1].set_yticklabels([''])  # Remove horizontal label

axes[0, 2].barh(['Humidity (%)'], [humidity], color='lightgreen')
axes[0, 2].set_title(f"Location: {city} - Humidity: {humidity}%")
axes[0, 2].set_yticklabels([''])  # Remove horizontal label

axes[1, 0].barh(['Wind Speed (m/s)'], [wind_speed], color='purple')
axes[1, 0].set_title(f"Location: {city} - Wind Speed: {wind_speed} m/s")
axes[1, 0].set_yticklabels([''])  # Remove horizontal label

axes[1, 1].barh(['Cloud Coverage (%)'], [cloud_coverage], color='lightcoral')
axes[1, 1].set_title(f"Location: {city} - Cloud Coverage: {cloud_coverage}%")
axes[1, 1].set_yticklabels([''])  # Remove horizontal label

axes[1, 2].barh(['Visibility (m)'], [visibility], color='lightskyblue')
axes[1, 2].set_title(f"Location: {city} - Visibility: {visibility} m")
axes[1, 2].set_yticklabels([''])  # Remove horizontal label

axes[2, 0].text(0.5, 0.5, f"Weather: {weather_description}", fontsize=12, ha='center')
axes[2, 0].set_title("Weather Description")
axes[2, 0].axis('off')  # Hide axes

axes[2, 1].text(0.5, 0.5, f"Sunrise: {sunrise_time}", fontsize=12, ha='center')
axes[2, 1].set_title("Sunrise")
axes[2, 1].axis('off')  # Hide axes

axes[2, 2].text(0.5, 0.5, f"Sunset: {sunset_time}", fontsize=12, ha='center')
axes[2, 2].set_title("Sunset")
axes[2, 2].axis('off')  # Hide axes

# Adjust the layout further for better fit
plt.subplots_adjust(hspace=0.7, wspace=0.7)  # Increase space between subplots

# Add vertical labels for each subplot
axes[0, 0].set_ylabel('Temperature (°C)', rotation=90, fontsize=12)  # Set the vertical label for Temperature
axes[0, 1].set_ylabel('Feels Like (°C)', rotation=90, fontsize=12)  # Set the vertical label for Feels Like
axes[0, 2].set_ylabel('Humidity (%)', rotation=90, fontsize=12)  # Set the vertical label for Humidity
axes[1, 0].set_ylabel('Wind Speed (m/s)', rotation=90, fontsize=12)  # Set the vertical label for Wind Speed
axes[1, 1].set_ylabel('Cloud Coverage (%)', rotation=90, fontsize=12)  # Set the vertical label for Cloud Coverage
axes[1, 2].set_ylabel('Visibility (m)', rotation=90, fontsize=12)  # Set the vertical label for Visibility

# Show the plots
plt.show()
