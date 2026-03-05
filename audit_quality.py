from google.cloud import bigquery
import pandas as pd

PROJECT_ID = "ntu-project-64847"
client = bigquery.Client(project=PROJECT_ID)

def run_data_quality_audit():
    print("--- 🛡️ Starting Data Quality Audit ---")
    
    # Check 1: Primary Key Uniqueness (The "show_id" test)
    # Validates the Business Value of "Single Source of Truth"
    pk_query = f"SELECT show_id, COUNT(*) as count FROM `{PROJECT_ID}.raw.movies` GROUP BY 1 HAVING count > 1"
    dupes = client.query(pk_query).to_dataframe()
    
    # Check 2: Relationship Integrity (The "Star Schema" test)
    # Ensures every movie has a valid location key
    fk_query = f"""
    SELECT COUNT(*) as orphans 
    FROM `{PROJECT_ID}.raw.movies` m
    LEFT JOIN `{PROJECT_ID}.raw.dim_locations` l ON m.location_key = l.location_key
    WHERE l.location_key IS NULL
    """
    orphans = client.query(fk_query).to_dataframe().iloc[0]['orphans']

    # --- Print Audit Report ---
    status = "✅ PASSED" if len(dupes) == 0 and orphans == 0 else "❌ FAILED"
    print(f"Data Integrity Status: {status}")
    print(f"- Duplicate IDs found: {len(dupes)}")
    print(f"- Orphaned records found: {orphans}")
    print("-" * 35)

if __name__ == "__main__":
    run_data_quality_audit()