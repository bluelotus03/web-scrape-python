from bs4 import BeautifulSoup
import requests

# Make the request to the url to get its content
page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of the page
page_title = soup.title.text # gets you the text of the <title>(...)</title>

#print(soup, title)

# Prints the title
print(page_title)