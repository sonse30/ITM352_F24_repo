# Define the survey responses and respondent IDs
survey_responses = [5, 7, 3, 8]
respondent_ids = (1012, 1035, 1021, 1053)

# Use zip() to create a dictionary with IDs as keys and responses as values
survey_dict = dict(zip(respondent_ids, survey_responses))

# Print the dictionary
print("Survey Dictionary:", survey_dict)
