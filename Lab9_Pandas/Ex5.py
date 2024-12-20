import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('home_data.csv')


print("Dimensions of the DataFrame:", df.shape)

# Show the first 10 rows
print("First 10 rows:")
print(df.head(10))

