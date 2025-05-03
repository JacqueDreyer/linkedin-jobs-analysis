import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv('data/clean_jobs.csv')

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Drop completely empty columns
df.dropna(axis=1, how='all', inplace=True)

# Strip text fields
text_fields = ['title', 'company', 'location', 'description']
for col in text_fields:
    df[col] = df[col].astype(str).str.strip()

# Convert date
if 'date_posted' in df.columns:
    df['date_posted'] = pd.to_datetime(df['date_posted'], errors='coerce')

# Output folder
os.makedirs('output', exist_ok=True)

# Export cleaned data
df.to_excel('output/cleaned_jobs.xlsx', index=False)

print("✅ Cleaned dataset saved to output/cleaned_jobs.xlsx")

# Most common job titles
top_titles = df['title'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_titles.values, y=top_titles.index, palette='crest')
plt.title('Top 10 Most Common Job Titles')
plt.xlabel('Count')
plt.tight_layout()
plt.savefig('output/top_job_titles.png')
plt.close()

# Most common job locations
top_locations = df['location'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_locations.values, y=top_locations.index, palette='magma')
plt.title('Top 10 Job Locations')
plt.xlabel('Count')
plt.tight_layout()
plt.savefig('output/top_job_locations.png')
plt.close()

print("📊 Plots saved to output folder.")