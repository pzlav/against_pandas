import time
import polars as pl
from datetime import datetime
import sys

# Check if the filename is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python script_name.py <filename>")
    sys.exit(1)

# Get the filename from the command-line arguments
filename = sys.argv[1]


start_time = time.time()


q = (
    pl.scan_csv(filename)
    .filter(pl.col("value") > 35)
    .group_by("username")
    .agg(pl.col("value").mean())
)
df = q.collect()
print(df)



end_time = time.time()
execution_time = end_time - start_time


print(f"Start Time: {datetime.fromtimestamp(start_time)}")
print(f"End Time: {datetime.fromtimestamp(end_time)}")
print(f"Execution Time: {execution_time // 3600} hours, {(execution_time % 3600) // 60} minutes, {execution_time % 60} seconds")
