
import requests
from bs4 import BeautifulSoup
import os

base_url = "http://127.0.0.1:4443/.hidden/"

def get_readme_files(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    readme_files = []

    for link in soup.find_all('a'):
        href = link.get('href')
        if href.endswith('/') and not href.startswith('.'):
            readme_files.extend(get_readme_files(os.path.join(url, href)))
        elif href.lower() == 'readme':
            readme_files.append(os.path.join(url, href))
            
    return readme_files

readme_files = get_readme_files(base_url)
f = open("readme_files.txt", "w")
for readme in readme_files:
    content = requests.get(readme).text
    if "flag" in content: 
    	f.write(content + "\n")