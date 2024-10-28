import pandas as pd
import pyarrow.csv as pv
import time


# URL of the CSV file
#url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"
url = "sales_data_test.csv"

try:
   # Read the CSV file using PyArrow and convert it to a Pandas DataFrame
   print("CSV File is loading...")
   
   time_start = time.time()
   
   df = pd.read_csv(url, dtype_backend='pyarrow', on_bad_lines = 'skip')
   
   df.to_csv('sales_data_test.csv')
   
    #replace missing data with 0's
   df.fillna(0, inplace = True)
   
   print(df.head(10))
   print (f"CSV File Loaded in { (time.time() - time_start) } seconds")
   


except ValueError as ve:
   print(f"Error: {ve}")
except FileNotFoundError:
   print("Error: The file could not be found.")
except Exception as e:
   print(f"An unexpected error occurred: {e}")