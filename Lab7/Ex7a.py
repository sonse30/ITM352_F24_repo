# Given tuples
years_tuple = (1980, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989)
respondents_tuple = (17, 35, 26, 26, 25, 27, 35, 21, 19)

# Initialize empty lists
years_list = []
respondents_list = []

# Iterate through the years tuple and append to years_list
for year in years_tuple:
    years_list.append(year)

# Iterate through the respondents tuple and append to respondents_list
for respondent in respondents_tuple:
    respondents_list.append(respondent)

# Create a dictionary with the lists
data_dict = {
    "years": years_list,
    "respondents": respondents_list
}

# Print the dictionary to verify
print(data_dict)
