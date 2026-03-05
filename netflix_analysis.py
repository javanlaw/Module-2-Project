from google.cloud import bigquery
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Setup Connection
PROJECT_ID =  "ntu-project-64847" # REPLACE WITH YOUR ID
client = bigquery.Client(project=PROJECT_ID)

def fetch_business_data():
    # Joining the 3 transformed files to fulfill the Business Case
    query = f"""
    SELECT 
        m.title,
        m.release_year,
        d.director_name,
        l.country,
        m.rating
    FROM `{PROJECT_ID}.raw.movies` m
    JOIN `{PROJECT_ID}.raw.dim_directors` d ON m.director_key = d.director_key
    JOIN `{PROJECT_ID}.raw.dim_locations` l ON m.location_key = l.location_key
    """
    return client.query(query).to_dataframe()

def generate_insights(df):
    # Insight 1: Regional Content Strategy (Business Value: Market Analysis)
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, y='country', order=df['country'].value_counts().index[:10], palette='magma')
    plt.title('Business Insight: High-Priority Content Markets')
    plt.xlabel('Volume of Content Produced')
    plt.show()

    # Insight 2: Director Productivity (Business Value: Talent Analytics)
    # print("\n--- Strategic Talent Report: Top 5 Directors ---")
    # print(df['director_name'].value_counts().head(5))

    plt.figure(figsize=(12, 6))
    top_5 = df['director_name'].value_counts().head(5)
    sns.barplot(x=top_5.values, y=top_5.index, palette='viridis')
    
    plt.title('Talent Analytics: Top 5 Most Prolific Directors', fontsize=14)
    plt.xlabel('Total Titles Directed')
    plt.ylabel('Director Name')
    
    for i, v in enumerate(top_5.values):
        plt.text(v + 0.1, i, str(v), color='black', va='center', fontweight='bold')
    plt.tight_layout()
    plt.show()

    # Insight 3: Content Freshness (Business Value: Library Maturity)
    plt.figure(figsize=(12, 6))
    df_modern = df[df['release_year'] > 2010]
    sns.histplot(df_modern['release_year'], bins=11, kde=True, color='teal')
    plt.title('Business Insight: Library Recency Trend (Post-2010)')
    plt.show()

    # Insight 4: Movie Release Trends Over Time
    # plt.figure(figsize=(10, 6))
    # release_counts = df.groupby('release_year').size().reset_index(name='count')
    # sns.lineplot(data=release_counts, x='release_year', y='count', marker='o')
    # plt.title('Netflix Movie Release Trends')
    # plt.xlim(2000, 2021) # Focusing on modern era
    # plt.show()

if __name__ == "__main__":
    print("Connecting to BigQuery Star Schema...")
    data = fetch_business_data()
    generate_insights(data)
