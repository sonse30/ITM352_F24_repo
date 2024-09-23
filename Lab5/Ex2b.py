# Define the list of miles and the tuple of fares
trip_miles = [1.1, 0.8, 2.5, 2.6]
trip_fares = ("$6.25", "$5.25", "$10.50", "$8.05")

trips = dict(zip(trip_miles,trip_fares))

# Access and print the duration and fare for the 3rd trip
print(trips)

print(f"The 3rd trip's duration is {2.5} miles and it cost {trips [2.5]}.")
