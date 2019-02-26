from bs4 import BeautifulSoup
import requests

resp = requests.get('https://www.youtube.com/results?search_query=Good+Girl+Dustin+Lynch')
soup = BeautifulSoup(resp.text, "html.parser")

youtube = "https://www.youtube.com/embed/"
tags = soup.find_all("h3", {"class": "yt-lockup-title"})
tag = tags[0].find('a')['href']
tag = tag[9:len(tag)]
tag = youtube + tag

print(tag)
