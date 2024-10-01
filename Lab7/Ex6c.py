def check_fares(fares):
    """Check each fare and return a list of messages indicating if it's high or low."""
    messages = []
    for fare in fares:
        if fare > 12:
            messages.append("This fare is high!")
        else:
            messages.append("This fare is low.")
    return messages

# Sample fares list
sample_fares = [8.60, 5.75, 13.25, 21.21]

# Call the function with the sample fares and print the results
results = check_fares(sample_fares)
for result in results:
    print(result)

# Test cases
def test_check_fares():
    assert check_fares([10, 15, 5]) == ["This fare is low.", "This fare is high!", "This fare is low."]
    assert check_fares([12, 12.01, 12]) == ["This fare is low.", "This fare is high!", "This fare is low."]
    assert check_fares([13, 20, 30]) == ["This fare is high!", "This fare is high!", "This fare is high!"]
    assert check_fares([0, 2, 8, 11]) == ["This fare is low.", "This fare is low.", "This fare is low.", "This fare is low."]
    assert check_fares([]) == []  # Test with an empty list

# Run test cases
test_check_fares()

print("All test cases passed!")
