from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/01_Info_collecting/index.html"
req = Request(url)
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

subject = soup.find('h1').text
print(subject)

title = soup.find('header').text
print(title)

body = soup.find_all('div')
print(body)

id_ = soup.find(name='div', attrs={"class":"child1"}).text
print(id_)

pw_ = soup.find(name='div', attrs={'id':'child2'}).text
print(pw_)

link = soup.find('a', href=True)['href']
print(link)

# soup.find("태그명", attrs={"class/id":"name"})
# soup.find(attrs={"class":"btn"}) --> 유일한 class 값이라면 태그명이 빠져도 된다.