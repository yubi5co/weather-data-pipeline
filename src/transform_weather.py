import json
import pandas as pd

with open("data/weather.json", "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"],
    "humidity": data["hourly"]["relative_humidity_2m"],
    "precipitation": data["hourly"]["precipitation"]
})

print(df.head())

df.to_csv(
    "data/weather.csv",
    index=False,
    encoding="utf-8-sig"
)

print("CSV 저장 완료!")