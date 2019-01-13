import csv
from bs4 import BeautifulSoup
import requests

url = input("Enter a url to scrape: ")
lim = int(input('How many links do you want?'))
print('\n')

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a', limit=lim)

if links == []:
	print('No links')
	exit()

listOfText = list()
listOfURLs = list()
masterList = [['Text', 'URL']]

for a in links:
	if a.string != None:
		print(a.string+'- ',end ="")
		listOfText.append(a.string)
	else:
		listOfText.append('')
	print(str(a['href'])+'\n')
	listOfURLs.append(str(a['href']))

for i in range(0, len(listOfURLs)):
	masterList.append([listOfText[i], listOfURLs[i]])

outfile = open('./links.csv', 'w')
writer = csv.writer(outfile)
writer.writerows(masterList)
