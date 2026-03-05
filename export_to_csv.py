from google.cloud import bigquery
import pandas as pd

PROJECT_ID = "ntu-project-64847" # Same as in your load script
TABLE_ID = f"{PROJECT_ID}.raw.movies"

client = bigquery.Client(project=PROJECT_ID)

# Download the results to a DataFrame
sql = f"SELECT * FROM `{TABLE_ID}`"
df = client.query(sql).to_dataframe()

# Save to CSV in your current VS Code folder
df.to_csv("transformed_movies.csv", index=False)
print("Export complete: transformed_movies.csv")