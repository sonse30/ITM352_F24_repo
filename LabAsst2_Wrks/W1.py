import pandas as pd
import pyarrow.csv as pv


# URL of the CSV file
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"


try:
   # Read the CSV file using PyArrow and convert it to a Pandas DataFrame
   df = pd.read_csv(url, dtype_backend='pyarrow', on_bad_lines = 'skip')
   
   df.to_csv('sales_data_test.csv')
   
   print(df.head(10))


except ValueError as ve:
   print(f"Error: {ve}")
except FileNotFoundError:
   print("Error: The file could not be found.")
except Exception as e:
   print(f"An unexpected error occurred: {e}")