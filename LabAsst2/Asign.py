import pandas as pd
import pyarrow.csv as pv
import time

analytics_results = {}

# URL of the CSV file
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

try:
   # Read the CSV file using PyArrow and convert it to a Pandas DataFrame
   print("CSV File is loading...")
   
   #Add time feature to showcase waiting time
   time_start = time.time()
   
   df = pd.read_csv(url, dtype_backend='pyarrow', on_bad_lines = 'skip')
   
   df.to_csv('sales_data_test.csv')
   
   df.fillna(0, inplace = True)
   
   print(df.head(10))
   print (f"CSV File Loaded in { (time.time() - time_start) } seconds")
   
#Defensive coding in case of unexpected errors occur
except ValueError as ve:
   print(f"Error: {ve}")
except FileNotFoundError:
   print("Error: The file could not be found.")
except Exception as e:
   print(f"An unexpected error occurred: {e}")
   
sales_data = pd.read_csv("sales_data_test.csv")

#Finding the sales amount to fit the value needed that isn't shown in the csv
sales_data['sales'] = sales_data['quantity'] * sales_data['unit_price']

#Dashboard Section that AI has helped me w/ the prompt of the 1st, 2nd, & 3rd Assignments questions asked
def show_first_n_rows():
    print(f"\nThere are {len(sales_data)} rows available.")
    n = input("Enter rows to display:\n- Enter a number 1 to 5129\n- To see all rows, enter 'all'\n- To skip preview, press Enter\nYour choice: ")
    
    #Allows user to choose the amount of data seen with options
    if n.lower() == 'all':
        print(sales_data)
    elif n.isdigit() and 1 <= int(n) <= len(sales_data):
        print(sales_data.head(int(n)))
    elif n == '':
        print("Skipping preview.")
    #Defensive code if user chooses invalid input
    else:
        print("Invalid input. Please enter a valid number or 'all'.")

#AI used to correctly & quickly define each menu option w/ the prompt from R3
def total_sales_by_region_and_order_type():
    result = pd.pivot_table(sales_data, index="sales_region", columns="order_type", values="sales", aggfunc="sum")
    print(result)
    
#Usage of aggfunc to find the average for the rows & columns for the region
def average_sales_by_region_state_sale_type():
    result = pd.pivot_table(sales_data, index="sales_region", columns=["customer_state", "order_type"], values="sales", aggfunc="mean")
    print(result)

#Usage of aggfunc to find the sum for the rows & columns for the state
def sales_by_customer_and_order_type_by_state():
    result = pd.pivot_table(sales_data, index=["customer_state", "customer_type"], columns="order_type", values="sales", aggfunc="sum")
    print(result)
    
#Usage of aggfunc to find the sum for the rows & columns for the region product
def total_sales_quantity_price_by_region_product():
    result = pd.pivot_table(sales_data, index="sales_region", columns="produce_name", values=["quantity", "sales"], aggfunc="sum")
    print(result)

#Usage of aggfunc to find the sum for the rows & columns for the customer type
def total_sales_quantity_price_by_customer_type():
    result = pd.pivot_table(sales_data, index="customer_type", columns="order_type", values=["quantity", "sales"], aggfunc="sum")
    print(result)
    
#Usage of built in max & min functions for menu option
def max_min_sales_price_by_category():
    result = pd.pivot_table(sales_data, index="product_category", values="unit_price", aggfunc=["max", "min"])
    print(result)

#Usage of aggfunc=lambda x: x.nunique()) to find the unique employes within regions
def unique_employees_by_region():
    result = pd.pivot_table(sales_data, index="sales_region", values="employee_id", aggfunc=lambda x: x.nunique())
    print(result)
#Usage of AI for help in creating a effective summary for data within each menu option
def display_sales_data_summary(df):
    print("\n--- Sales Data Summary ---")
    
    summary = {}
    
    #Summary data for all 9 menu options (unique, max, min, sum)
    try:
        summary['Total Orders'] = len(df)
        summary['Unique Employees'] = df['employee_id'].nunique()
        summary['Sales Regions'] = df['sales_region'].nunique()
        summary['Order Dates Range'] = f"{df['order_date'].min()} to {df['order_date'].max()}"
        summary['Unique Customers'] = df['customer_id'].nunique()
        summary['Product Categories'] = df['product_category'].nunique()
        summary['Unique States'] = df['customer_state'].nunique()
        summary['Total Sales Amount'] = df['sales'].sum()
        summary['Total Quantities Sold'] = df['quantity'].sum()

        for key, value in summary.items():
            print(f"{key}: {value}")
    
    #Defensive code when occurence of missing data
    except KeyError as e:
        print(f"Warning: Column '{e.args[0]}' is missing. Some analytics might be unavailable.")
        # Remove menu items associated with missing columns
        if 'employee_id' not in df.columns:
            del menu_items["8"]  # Remove unique employees by region option
        if 'sales_region' not in df.columns or 'order_type' not in df.columns:
            del menu_items["2"]  # Remove total sales by region and order type option

#Definition for "select_options" used in the customizable pivot table generator
def select_options(options, prompt, allow_multiple=True, optional=False):
    print(prompt)
    for key, val in options.items():
        print(f"{key}. {val}")
    choice = input("Enter the number(s) of your choice(s), separated by commas" + (" (enter for no grouping): " if optional else ": "))
    
    selected = [options[num.strip()] for num in choice.split(",") if num.strip() in options]
    
    if not selected and not optional:
        print("No valid selections. Exiting custom pivot table generator.")
        return None
    return selected if allow_multiple else selected[0] if selected else None

# AI used for help creating a code for customizable pivot table generator function; asking the question from R4
def pivot_table_generator():
    print("\n--- Custom Pivot Table Generator ---")

    # Defines the avaiable option dictionaries for rows, columns, values, and aggregation functions
    row_options = {"1": "employee_name", "2": "sales_region", "3": "product_category"}
    col_options = {"1": "order_type", "2": "customer_type"}
    val_options = {"1": "quantity", "2": "sales"}
    agg_func_options = {"1": "sum", "2": "mean", "3": "count"}

    # Prompts user to select one or more rows for the unique pivot table
    rows = select_options(row_options, "Select rows:", allow_multiple=True)
    if rows is None: return
    
    #Prompts user to select one or more columns & values for the unique pivot table
    columns = select_options(col_options, "Select columns (optional):", allow_multiple=True, optional=True)
    values = select_options(val_options, "Select values:", allow_multiple=True)
    if values is None: return
    
    #Using AI, creating a agg function with the restriction of only one choice
    agg_func = select_options(agg_func_options, "Select aggregation function:", allow_multiple=False)
    if not agg_func:
        print("Invalid aggregation function. Exiting custom pivot table generator.")
        return

    # Generate Pivot Table if user selects one of the choices
    try:
        pivot_table = pd.pivot_table(
            sales_data,
            index=rows,
            columns=columns,
            values=values,
            aggfunc=agg_func
        )
        print("\nGenerated Pivot Table:\n")
        print(pivot_table)
           # Store pivot table in analytics_results dictionary
        analytics_key = f"Custom Pivot {len(analytics_results) + 1}"
        analytics_results[analytics_key] = pivot_table

        # AI generated code for an optional choice for the user to export the pivot table into excel; using the prompt about exporting the customized pivot table table into excel
        export_choice = input("Would you like to export this result to an Excel file? (yes/no): ").strip().lower()
        #Code to export the pivot into excel using an already created .xlsx sheet
        if export_choice == 'yes':
            filename = input("Enter the filename (e.g., 'pivot_table.xlsx'): ").strip()
            pivot_table.to_excel(filename)
            print(f"Pivot table exported to {filename}")
        #If the file is not found the pivot table will not be exported; promting user to create the file first before exporting10
        else:
            print("Pivot table not exported.")
    # Defensive coding if in case of error occurs with the pivot table creation
    except Exception as e:
        print(f"Error creating pivot table: {e}")

#Exit for dashboard and menu options
def exit_dashboard():
    print("Exiting the dashboard. Goodbye!")
    exit()

# AI used to efficiently organize my dashboard menu items into ordered dictionary w/ prompt to fit data into specific dashboard look
menu_items = {
    "1": ("Show the first n rows of sales data", show_first_n_rows),
    "2": ("Total sales by region and order_type", total_sales_by_region_and_order_type),
    "3": ("Average sales by region with average sales by state and sale type", average_sales_by_region_state_sale_type),
    "4": ("Sales by customer type and order type by state", sales_by_customer_and_order_type_by_state),
    "5": ("Total sales quantity and price by region and product", total_sales_quantity_price_by_region_product),
    "6": ("Total sales quantity and price by customer type", total_sales_quantity_price_by_customer_type),
    "7": ("Max and min sales price by category", max_min_sales_price_by_category),
    "8": ("Number of unique employees by region", unique_employees_by_region),
    "9": ("Create a custom pivot table", pivot_table_generator),
    "10": ("Exit", exit_dashboard)
}

#Dashboard Header for the Menu screen
def display_menu():
    print("\n--- Sales Data Dashboard ---")
    for key, (description, _) in menu_items.items():
        print(f"{key}. {description}")

#Created loop for user to go back to menu when finished with an option
def main():
    while True:
        display_menu()
        choice = input("Select a menu option by entering the number: ")
        if choice in menu_items:
            _, action = menu_items[choice]
            action()
        else:
            print("Invalid choice. Please select a valid menu option.")

if __name__ == "__main__":
    main()