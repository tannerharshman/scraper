import urllib.request
import re
import requests
from bs4 import BeautifulSoup



url = "http://theoatmeal.com"
response = urllib.request.urlopen(url)
content = response.read()
soup = BeautifulSoup(content, "html.parser")

for link in soup.findAll("a"):
    my_url = link.get('href')
    if re.search("http", my_url):
        print(my_url)

images = soup.findAll("img")
for image in images:
    my_image = image.get('src')
    print(f"{url}{my_image}")
