import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# ---- Configuration ----
API_KEY = "2f0dbd93d0961c164232ec60957a94de"  # Replace with your actual API key
CITY = "Mumbai"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# ---- API Request ----
response = requests.get(URL)

# ---- Error Handling ----
if response.status_code != 200:
    print(f"Error fetching data: {response.status_code} - {response.text}")
    exit()

data = response.json()

# ---- Data Parsing ----
dates, temperatures, humidities = [], [], []

for entry in data['list']:
    dt = datetime.fromtimestamp(entry['dt'])
    temp = entry['main']['temp']
    humidity = entry['main']['humidity']

    dates.append(dt)
    temperatures.append(temp)
    humidities.append(humidity)

# ---- Set Plot Style ----
sns.set(style="darkgrid")

# ---- Plot Temperature ----
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temperatures, marker="o", color="orange")
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temperature_plot.png")
plt.show()

# ---- Plot Humidity ----
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=humidities, marker="s", color="blue")
plt.title(f"Humidity Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("humidity_plot.png")
plt.show()
