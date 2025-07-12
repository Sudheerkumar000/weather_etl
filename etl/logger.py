import csv
from datetime import datetime

def log_to_csv(data, file_path="weather_log.csv"):
    headers = ['timestamp', 'temperature', 'description', 'humidity', 'wind_speed']
    row = [
        datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        data['temperature'],
        data['description'],
        data['humidity'],
        data['wind_speed']
    ]

    try:
        print("✅ Writing to:", file_path)
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerow(row)
            print("✅ CSV file created and written successfully.")
    except Exception as e:
        print(f"❌ Error writing to CSV: {e}")
