import urllib.request
import re
import os
import requests
from bs4 import BeautifulSoup


def dl_image(url, folder_path):
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.basename(url)
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded and saved: {file_path}")
    else:
        print(f"Failed to download: {url}")


a_url = "http://theoatmeal.com"
a_response = urllib.request.urlopen(a_url)
content = a_response.read()
soup = BeautifulSoup(content, "html.parser")

for link in soup.findAll("a"):
    my_url = link.get('href')
    if re.search("http", my_url):
        print(my_url)

images = soup.findAll("img")
download_folder = "oatmeal_pics"

if not os.path.exists(download_folder):
    os.mkdir(download_folder)

for image in images:
    my_image = image.get('src')
    if my_image and re.search(r"^http", my_image):
        print(f"{my_image}")  # Print the image URL
        dl_image(my_image, download_folder)
