import pandas as pd
import pyarrow.csv as pv

# Set Pandas display option to show all columns
pd.set_option('display.max_columns', None)

# URL of the CSV file
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

try:
    df = pd.read_csv(url, dtype_backend='pyarrow', on_bad_lines='skip')
    
    df['total_sales'] = df['unit_price'] * df['quantity']

    # Creating the pivot table by sales_region and order_type
    pivot_table = pd.pivot_table(
        df,
        values='total_sales',            # Aggregating total sales
        index='sales_region',            # Rows are grouped by sales_region
        columns='order_type',            # Columns are defined by order_type (Retail or Wholesale)
        aggfunc='sum',                   # Sum of sales in each group
        fill_value=0                     # Fill missing values with 0
    )

    # Print the pivot table
    print("Pivot Table: Sales by Region and Order Type")
    print(pivot_table)

except ValueError as ve:
    print(f"Error: {ve}")
except FileNotFoundError:
    print("Error: The file could not be found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
