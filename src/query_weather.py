import duckdb

query = """
SELECT
    time,
    temperature
FROM 'data/weather.csv'
WHERE temperature >= 25
"""

result = duckdb.sql(query)

print(result)