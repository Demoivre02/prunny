
import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A'],
    'Value': [10, 15, 7, 12, 9, 14, 8, 11, 13, 6],
    'Time': pd.date_range(start='2023-01-01', periods=10, freq='D')
}
df = pd.DataFrame(data)


plt.figure(figsize=(10, 5))
df['Category'].value_counts().plot(kind='bar')
plt.title('Frequency of Categories')
plt.xlabel('Category')
plt.ylabel('Count')
plt.savefig('/tmp/outputs/category_frequency.png')
plt.close()


plt.figure(figsize=(10, 5))
plt.plot(df['Time'], df['Value'], marker='o')
plt.title('Trend of Value Over Time')
plt.xlabel('Time')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/tmp/outputs/value_trend.png')
plt.close()

print("Bar chart saved as 'category_frequency.png' and line chart saved as 'value_trend.png' in the outputs folder.")