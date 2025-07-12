def transform_weather_data(data):
    try:
        transformed = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return transformed
    except KeyError as e:
        print(f"❌ Missing field in data: {e}")
        return None
