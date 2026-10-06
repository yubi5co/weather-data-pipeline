import requests
import json

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 35.6762,
    "longitude": 139.6503,
    "hourly": [
        "temperature_2m",
        "relative_humidity_2m",
        "precipitation"
    ],
    "timezone": "Asia/Tokyo"
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()

with open("data/weather.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("시간별 날씨 데이터 저장 완료!")