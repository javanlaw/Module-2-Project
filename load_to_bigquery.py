from google.cloud import bigquery
import pandas as pd

PROJECT_ID = "ntu-project-64847"
TABLE = "raw.netflix_titles"
FILE = "netflix_titles.csv"

client = bigquery.Client(project=PROJECT_ID)

df = pd.read_csv(FILE)

table_id = f"{PROJECT_ID}.{TABLE}"
job = client.load_table_from_dataframe(df, table_id)
job.result()

print("Loaded", len(df), "rows into", table_id)