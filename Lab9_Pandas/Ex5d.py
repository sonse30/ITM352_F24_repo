import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('home_data.csv')

# Drop rows with null values
df_cleaned = df.dropna()

# Drop duplicate rows
df_cleaned = df_cleaned.drop_duplicates()

# Show cleaned DataFrame
print("Cleaned DataFrame after dropping nulls and duplicates:")
print(df_cleaned.head(10))
