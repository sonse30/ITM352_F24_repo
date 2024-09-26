def determine_progress1(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio > 0:
        progress = "On your way!"
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            if hits_spins_ratio >= 0.5:
                if hits < spins:
                    progress = "You win!"
    else:
        progress = "Get going!"

    return progress

def test_determine_progress(progress_function):
       # Test case 1: spins == 0, should return "Get going!"
    assert determine_progress1(0, 0) == "Get going!", "Test Case 1 Failed"
    
    # Test case 2: hits == 0 and spins > 0, should return "Get going!"
    assert determine_progress1(0, 5) == "Get going!", "Test Case 2 Failed"
    
    # Test case 3: hits / spins is positive but less than 0.25, should return "On your way!"
    assert determine_progress1(1, 5) == "On your way!", "Test Case 3 Failed"
    
    # Test case 4: hits / spins is between 0.25 and 0.5, should return "Almost there!"
    assert determine_progress1(2, 5) == "Almost there!", "Test Case 4 Failed"
    
    # Test case 5: hits / spins is greater than or equal to 0.5, but hits < spins, should return "You win!"
    assert determine_progress1(3, 5) == "You win!", "Test Case 5 Failed"

    # Test case 6: hits / spins is exactly 0.25, should return "Almost there!"
    assert determine_progress1(1, 4) == "Almost there!", "Test Case 6 Failed"

    # Test case 7: hits / spins is exactly 0.5, should return "You win!"
    assert determine_progress1(5, 10) == "You win!", "Test Case 7 Failed"

    print("All test cases passed!")

test_determine_progress(determine_progress1)
