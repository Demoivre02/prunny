import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 18, 40]
}
df = pd.DataFrame(data)

df['IsAdult'] = df['Age'] >= 18

print(df)