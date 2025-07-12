
import csv
import os
from dotenv import load_dotenv
load_dotenv()

print("🧪 Loaded API_KEY:", os.getenv("API_KEY"))
print("🧪 Loaded AWS Key ID:", os.getenv("AWS_ACCESS_KEY_ID"))

from etl.extract import fetch_weather
from etl.transform import transform_weather_data
from etl.logger import log_to_csv
from etl.upload_to_s3 import upload_to_s3
from datetime import datetime


def log_to_csv(data, file_path='weather_log.csv'):
    headers = ['timestamp', 'temperature', 'description', 'humidity', 'wind_speed']
    row = [
        datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        data['temperature'],
        data['description'],
        data['humidity'],
        data['wind_speed']
    ]

    try:
        with open(file_path, 'w', newline='') as f:  # change 'x' to 'w'
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerow(row)
            print("✅ CSV file created and written successfully.")  # 👈 Paste here

    except FileExistsError:
        with open(file_path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(row)
            print("✅ CSV row appended successfully.")  # optional: for append case


if __name__ == '__main__':
    raw_data = fetch_weather()

    if raw_data:
        transformed = transform_weather_data(raw_data)

        if transformed:
            print("🐍 Transformed data:", transformed)
            log_to_csv(transformed)  # ✅ Log the data to CSV
            print("📁 Data written to weather_log.csv")

            print("🚀 Trying to upload file to S3...")
            upload_to_s3()  # ✅ Upload to S3
            print("✅ Upload function completed.")
