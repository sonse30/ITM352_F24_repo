import requests
from bs4 import BeautifulSoup

# Fetch the page
url = "https://shidler.hawaii.edu/itm/people"
response = requests.get(url)
page_content = response.content

# Parse with BeautifulSoup
soup = BeautifulSoup(page_content, "html.parser")

# Print out a portion of the parsed HTML for inspection
print(soup.prettify()[:500])  # Shows the first 500 characters
