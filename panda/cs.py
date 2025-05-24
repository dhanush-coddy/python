import pandas as pd


data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [30, 25, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)


df.to_csv('example.csv', index=False)

print("CSV file saved!")
