import requests
from bs4 import BeautifulSoup

url = "https://shidler.hawaii.edu/itm/people"
response = requests.get(url)
page_content = response.content

soup = BeautifulSoup(page_content, "html.parser")

# Assume people are listed under a specific tag, e.g., <div class="people-name">
people_tags = soup.find_all("div", class_="people-name")

# Extract people names
people = [person.get_text(strip=True) for person in people_tags]

# Print the results
print("People found:", people)
print("Number of people:", len(people))
