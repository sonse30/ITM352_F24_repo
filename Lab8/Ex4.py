import csv

# Initialize variables
total_fare = 0.00
minimum_fare = float('inf')  # Set to infinity for comparison
maximum_trip_distance = 0
line_number = 0
valid_fare_count = 0  # To calculate the average fare

# Open the CSV file
with open('taxi_1000.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    for line in csv_reader:
        # Skip the header (first line)
        if line_number > 0:
            try:
                # Extract fare, trip miles, and total
                fare = float(line[10])  # fare is in column 10
                trip_miles = float(line[5])  # trip miles in column 5
                trip_total = float(line[14])  # total fare in column 14

                # Only include fares greater than $10
                if fare > 10:
                    total_fare += fare
                    valid_fare_count += 1

                    # Find the minimum fare greater than 0
                    if 0 < trip_total < minimum_fare:
                        minimum_fare = trip_total

                    # Find the maximum trip distance
                    if trip_miles > maximum_trip_distance:
                        maximum_trip_distance = trip_miles

            except ValueError:
                # Skip lines with invalid or missing data
                print(f"Warning: Skipped invalid data on line {line_number + 1}")

        line_number += 1

# Print results
if valid_fare_count > 0:
    average_fare = total_fare / valid_fare_count
    print(f"The total of all fares over $10 is: ${total_fare:.2f}")
    print(f"The average fare (over $10) is: ${average_fare:.2f}")
    print(f"The minimum fare is: ${minimum_fare:.2f}")
    print(f"The maximum trip distance (for fares over $10) was {maximum_trip_distance:.2f} miles")
else:
    print("No valid fares over $10 were found.")
