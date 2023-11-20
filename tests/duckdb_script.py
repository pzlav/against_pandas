import duckdb
import time
from datetime import datetime
import sys

# Check if the filename is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python script_name.py <filename>")
    sys.exit(1)

# Get the filename from the command-line arguments
filename = sys.argv[1]

start_time = time.time()

# Connect to an in-memory DuckDB database
conn = duckdb.connect()

# Read the CSV file into DuckDB
conn.execute(f"CREATE VIEW csvdataset AS SELECT * FROM read_csv_auto('{filename}')")

# Perform the filtering and aggregation using DuckDB's SQL syntax
result = conn.execute("""
    SELECT username, AVG(value) AS avg_value
    FROM csvdataset
    WHERE value > 35
    GROUP BY username
""").fetchdf()

print(result)

end_time = time.time()
execution_time = end_time - start_time

print(f"Start Time: {datetime.fromtimestamp(start_time)}")
print(f"End Time: {datetime.fromtimestamp(end_time)}")
print(f"Execution Time: {execution_time // 3600} hours, {(execution_time % 3600) // 60} minutes, {execution_time % 60} seconds")
