# 🌦️ Weather ETL Project

This project is a simple ETL (Extract, Transform, Load) pipeline that collects real-time weather data using the OpenWeatherMap API, transforms it, logs it to a CSV file, and uploads it to AWS S3.

---

## 🔧 Tools & Technologies

- **Python 3.11**
- **OpenWeatherMap API**
- **AWS S3 (Boto3)**
- **Pandas**
- **Docker**
- **Git & GitHub**
- **PyCharm IDE**

---

## ⚙️ How It Works

1. **Extract**: Weather data is pulled from OpenWeatherMap using a city name.
2. **Transform**: Required fields are selected and renamed.
3. **Load**: Data is:
   - Logged to a local `weather_log.csv` file
   - Uploaded to an AWS S3 bucket

---

## 🧪 Running the Project

```bash
# Clone the repository
git clone https://github.com/Sudheerkumar000/weather_etl.git
cd weather_etl

# Create a virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Add your environment variables in .env
API_KEY=your_api_key_here
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key

# Run the pipeline
python main.py
