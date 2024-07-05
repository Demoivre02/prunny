import pandas as pd

# Create a Pandas DataFrame with columns Name (string) and Age (integer)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 18, 40]
}
df = pd.DataFrame(data)

# Add a new column IsAdult (boolean) indicating whether Age is greater than or equal to 18
df['IsAdult'] = df['Age'] >= 18

print(df)