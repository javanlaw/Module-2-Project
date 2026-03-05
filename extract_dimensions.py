from google.cloud import bigquery
import pandas as pd

# Use the Project ID from your load_to_bigquery.py script
PROJECT_ID = "ntu-project-64847" 

def export_table(table_name):
    client = bigquery.Client(project=PROJECT_ID)
    
    # Tables are located in the 'raw' dataset as defined in schema.yml
    table_id = f"{PROJECT_ID}.raw.{table_name}"
    
    print(f"Extracting {table_id}...")
    
    query = f"SELECT * FROM `{table_id}`"
    df = client.query(query).to_dataframe()
    
    file_name = f"{table_name}.csv"
    df.to_csv(file_name, index=False)
    print(f"Successfully saved to {file_name}")

# Export both dimension tables
export_table("dim_directors")
export_table("dim_locations")