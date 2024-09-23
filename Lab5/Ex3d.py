# Define the list of miles and the tuple of numeric fares
trip_fares_numeric = [6.25, 5.25, 10.50, 8.05]

# Use zip to create a list of dictionaries with numeric fares
trip_list_numeric = [{"duration": miles, "fare": fare} for miles, fare in zip(trip_miles, trip_fares_numeric)]

# Print the list of dictionaries with numeric fares
print("List of dictionaries with numeric fares:", trip_list_numeric)

# Access and print the duration and fare for the 3rd trip with numeric fare
third_trip_numeric = trip_list_numeric[2]
print(f"The 3rd trip's duration is {third_trip_numeric['duration']} miles and it cost ${third_trip_numeric['fare']}.")
