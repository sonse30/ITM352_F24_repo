def check_fares(fares):
    """Check each fare and print if it's high or low."""
    for fare in fares:
        if fare > 12:
            print("This fare is high!")
        else:
            print("This fare is low.")

# Sample fares list
sample_fares = [8.60, 5.75, 13.25, 21.21]

# Call the function with the sample fares
check_fares(sample_fares)
