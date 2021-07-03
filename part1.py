import requests

# Requests contents from the website you specify
# and assigns it to the res variable
#res = requests.get('https://codedamn.com')
res = requests.get('https://ifconfig.co/json')

# prints the corresponding attributes of the content
print(res.text)
print(res.status_code)