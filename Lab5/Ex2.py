# Define the list of miles and the tuple of fares
trip_miles = [1.1, 0.8, 2.5, 2.6]
trip_fares = ("$6.25", "$5.25", "$10.50", "$8.05")

# Store them in a dictionary
trips = {
    "miles": trip_miles,
    "fares": trip_fares
}

# Print the dictionary
print("Trips Dictionary:", trips)

# Access and print the duration and fare for the 3rd trip
third_trip_miles = trips["miles"][2]
third_trip_fare = trips["fares"][2]
print(f"The 3rd trip's duration is {third_trip_miles} miles and it cost {third_trip_fare}.")
