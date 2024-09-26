def determine_progress6(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins
    
    # List of conditions and their corresponding progress results
    conditions = [
        (hits_spins_ratio >= 0.5 and hits < spins, "You win!"),
        (hits_spins_ratio >= 0.25, "Almost there!"),
        (hits_spins_ratio > 0, "On your way!"),
        (hits_spins_ratio <= 0, "Get going!")
    ]
    
    # Loop over conditions and return the first that is True
    for condition, result in conditions:
        if condition:
            return result

def test_determine_progress(progress_function):
    assert progress_function(0, 0) == "Get going!", "Test Case 1 Failed"
    assert progress_function(0, 5) == "Get going!", "Test Case 2 Failed"
    assert progress_function(1, 5) == "On your way!", "Test Case 3 Failed"
    assert progress_function(2, 5) == "Almost there!", "Test Case 4 Failed"
    assert progress_function(3, 5) == "You win!", "Test Case 5 Failed"
    assert progress_function(1, 4) == "Almost there!", "Test Case 6 Failed"
    assert progress_function(5, 10) == "You win!", "Test Case 7 Failed"
    print("All test cases passed!")

test_determine_progress(determine_progress6)
