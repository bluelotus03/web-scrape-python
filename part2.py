import requests

# Get the contents of the url and assign to res
res = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

# Store text response of the content in txt
txt = res.text
# Store the status code of the content in status
status = res.status_code

# Print txt and status
# Can also print in one statement using print(txt, status)
print(txt)
print(status)