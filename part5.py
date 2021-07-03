from bs4 import BeautifulSoup
import requests

# Make the request to the url to get its content
page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extract all the <h1> text available (type will be bs4.element.ResultSet)
#first_h1 = soup.select('h1')

#Extract the first <h1> (type will be bs4.element.Tag)
#first_h1 = soup.select('h1')[0]

# Extract the first <h1> and show just the text (type will be 'str')
first_h1 = soup.select('h1')[0].text

# Prints the type of the <h1> 
print(type(first_h1))
# Prints the first <h1>
print(first_h1)