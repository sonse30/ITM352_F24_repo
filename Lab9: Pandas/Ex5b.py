import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('home_data.csv')

# Filter properties with 500 or more units
filtered_df = df[df['units'] >= 500]

# Drop unnecessary columns (replace 'Column1', 'Column2' with actual column names)
columns_to_drop = ['block', 'lot', 'gross_sqft', 'year_built', 'sale_price', 'land_sqft']
filtered_df = filtered_df.drop(columns=columns_to_drop)

# Show the first 10 rows of the filtered DataFrame
print("Filtered DataFrame - First 10 rows:")
print(filtered_df.head(10))
