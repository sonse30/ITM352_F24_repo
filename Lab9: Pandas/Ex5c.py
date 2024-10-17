import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('home_data.csv')

# Check data types before cleaning
print("Data Types Before Cleaning:")
print(df.dtypes)

# Convert incorrect data types (use appropriate conversions based on your data)
# Example: converting 'Units' to numeric and 'Price' to numeric if needed
df['Units'] = pd.to_numeric(df['units'], errors='coerce')  # Convert Units to numeric
df['Price'] = pd.to_numeric(df['sale_price'], errors='coerce')  # Convert Price to numeric

# Check the data types again
print("Data Types After Cleaning:")
print(df.dtypes)
