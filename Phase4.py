
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('train13519.csv')

# Bar Chart (first 10 records)
plt.figure(figsize=(10, 5))
plt.bar(df['timestamp'][:10], df['hourly_traffic_count'][:10], color='red')
plt.xticks(rotation=45, ha='right')
plt.title('Hourly Traffic Count (Bar Chart)')
plt.xlabel('Timestamp')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Scatter Plot (first 100 records)
plt.figure(figsize=(10, 5))
plt.scatter(df['timestamp'][:100], df['hourly_traffic_count'][:100])
plt.xticks(rotation=45, ha='right')
plt.title('Hourly Traffic Count (Scatter Plot)')
plt.xlabel('Timestamp')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

