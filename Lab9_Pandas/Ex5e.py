import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('home_data.csv')

# Check the actual column names to verify the existence of 'sale_price'
print("Columns in DataFrame:", df.columns)

# If necessary, strip leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Ensure 'sale_price' is the correct column name. Adjust if necessary.
if 'sale_price' not in df.columns:
    print("Error: 'sale_price' column not found in the dataset.")
else:
    # Convert 'sale_price' to numeric, coercing errors (non-numeric values will become NaN)
    df['sale_price'] = pd.to_numeric(df['sale_price'], errors='coerce')

    # Drop rows with null values and duplicates before filtering
    df_cleaned = df.dropna(subset=['sale_price']).drop_duplicates()

    # Filter out rows where sale_price is 0 or less
    df_sales_filtered = df_cleaned[df_cleaned['sale_price'] > 0]

    # Compute the average sales price
    average_sales_price = df_sales_filtered['sale_price'].mean()

    print("Average Sales Price:", average_sales_price)
