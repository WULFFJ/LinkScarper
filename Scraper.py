from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

#Headers used to appear as if its coming from a browser to not be stopped like its a bot

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}


#provokes an input to type in a full https address
url=input("Site Address:")
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
SCHEMES = ('http://', 'https://')

links = []

for tag in soup.find_all('a', href=True):
        links.append(tag['href'])

for link in links:
    if link.startswith('/',0):
        links.remove(link)



print(links)
#Specify your directory here to get the results as CSV

with open('/python/pythonlinks/python_link.csv', 'w') as csvFile:
    file_writer = csv.writer(csvFile)
    file_writer.writerow(links)
csvFile.close()
