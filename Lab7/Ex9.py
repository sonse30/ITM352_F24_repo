for number in range(1, 11):
    if number == 5:
        continue  # Skip the rest of the loop for number 5
    if number == 8:
        print("Stopping the loop at 8.")
        break  # Stop the loop entirely when reaching 8
    print(number)  # Print the number if it's not 5
