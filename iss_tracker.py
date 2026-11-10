import requests
import time
from datetime import datetime

url = "http://api.open-notify.org/iss-now.json"

print("\n🚀 ISS LIVE TRACKER")
print("==============================")
print("Press Ctrl + C to stop tracking")

try:
    while True:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]

        timestamp = data["timestamp"]
        current_time = datetime.fromtimestamp(timestamp)

        print("\n🌍 ISS CURRENT LOCATION")
        print("------------------------------")
        print(f"Latitude  : {latitude}")
        print(f"Longitude : {longitude}")
        print(f"Date      : {current_time.strftime('%d-%m-%Y')}")
        print(f"Time      : {current_time.strftime('%I:%M:%S %p')}")
        print("------------------------------")

        time.sleep(5)

except KeyboardInterrupt:
    print("\nISS Tracking Stopped!")

except requests.exceptions.RequestException as e:
    print("API Connection Error:", e)